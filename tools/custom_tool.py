"""
Custom tool implementation for Hello World Agent
"""

class CustomTool:
    """A base class for custom tools"""
    def __init__(self, name=None, description=None):
        self.name = name or "CustomTool"
        self.description = description or "A custom tool for the agent"

    def run(self, *args, **kwargs):
        return "Custom tool execution placeholder"