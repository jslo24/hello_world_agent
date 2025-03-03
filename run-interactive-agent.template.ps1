# PowerShell script to run the interactive agent container
# Replace with your actual OpenRouter API key
$env:OPENROUTER_API_KEY="your_openrouter_api_key_here"

# Build the interactive agent container
Write-Host "Building interactive agent container..." -ForegroundColor Cyan
docker build -t hello-agent-interactive -f Dockerfile-Interactive .

# Run the container with the API key
Write-Host "Starting interactive agent..." -ForegroundColor Green
docker run -it -e OPENROUTER_API_KEY=$env:OPENROUTER_API_KEY hello-agent-interactive
