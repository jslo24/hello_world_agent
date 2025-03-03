FROM python:3.9-slim

WORKDIR /app

# Install git and other dependencies
RUN apt-get update && apt-get install -y git

# Clone the repository
RUN git clone https://github.com/ruvnet/hello_world_agent.git /app/hello_world_agent

# Set working directory to the repository
WORKDIR /app/hello_world_agent

# Install fixed versions of dependencies to avoid conflicts
RUN pip install --upgrade pip
RUN pip install "langchain==0.0.335" 
RUN pip install "crewai==0.1.0" 
RUN pip install "anthropic==0.5.0" 
RUN pip install "openai==0.28.1" 
RUN pip install "python-dotenv>=1.0.0" "pyyaml>=6.0.0" "httpx>=0.24.0"

# Now install the package in development mode
RUN pip install -e .

# Create tools directory and add necessary files
RUN mkdir -p /app/hello_world_agent/tools

# Create necessary tool modules
RUN echo 'class CustomTool:\n    def __init__(self, name=None, description=None):\n        self.name = name or "CustomTool"\n        self.description = description or "A custom tool for the agent"\n\n    def run(self, *args, **kwargs):\n        return "Custom tool execution placeholder"' > /app/hello_world_agent/tools/custom_tool.py

RUN echo 'def get_human_input(prompt="Please provide your input:"):\n    print(f"\\n{prompt}")\n    return input("> ")\n\ndef validate_human_input(input_text, validation_func=None):\n    if validation_func:\n        return validation_func(input_text)\n    return True' > /app/hello_world_agent/tools/human_input.py

RUN touch /app/hello_world_agent/tools/__init__.py

# Copy environment variables file
COPY .env /app/hello_world_agent/.env

# Copy our interactive agent script
COPY interactive_agent.py /app/hello_world_agent/

# Set PYTHONPATH to include the current directory
ENV PYTHONPATH=/app/hello_world_agent

# Run the interactive agent
CMD ["python", "interactive_agent.py"]