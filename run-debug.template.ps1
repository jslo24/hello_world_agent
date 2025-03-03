# PowerShell script to run the debug container
# Replace with your actual OpenRouter API key - make sure there are no extra spaces!
$env:OPENROUTER_API_KEY="your_openrouter_api_key_here"

# Print a masked version of the key for verification
$masked_key = $env:OPENROUTER_API_KEY.Substring(0, 4) + "..." + $env:OPENROUTER_API_KEY.Substring($env:OPENROUTER_API_KEY.Length - 4)
Write-Host "Using OpenRouter API key: $masked_key" -ForegroundColor Yellow

# Build the debug container
Write-Host "Building debug container..." -ForegroundColor Cyan
docker build -t hello-agent-debug -f Dockerfile-Debug .

# Run the container with the API key properly quoted and formatted
Write-Host "Starting debug container..." -ForegroundColor Green
docker run -it -e "OPENROUTER_API_KEY=$env:OPENROUTER_API_KEY" hello-agent-debug