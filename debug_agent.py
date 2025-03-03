"""
Debug Agent - Tests OpenRouter API connectivity
"""
import os
import json
import httpx
from dotenv import load_dotenv

def test_openrouter_connection():
    """Test connection to OpenRouter API"""
    load_dotenv()  # Load variables from .env file
    
    # Get the API key
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        print("❌ ERROR: OPENROUTER_API_KEY not found in environment variables")
        print(f"Environment variables: {os.environ.keys()}")
        return False
    
    # Mask the key for display
    masked_key = api_key[:4] + "..." + api_key[-4:] if len(api_key) > 8 else "****"
    print(f"Using API key: {masked_key}")
    
    # Make a simple request to test the API
    try:
        print("\nTesting connection to OpenRouter API...")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",  # Required by OpenRouter
            "X-Title": "Hello World Agent Debug"
        }
        
        print(f"Request headers: {json.dumps(headers, default=str)}")
        
        # Make a simple API call
        response = httpx.get(
            "https://openrouter.ai/api/v1/auth/key",
            headers=headers,
            timeout=10.0
        )
        
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        
        if response.status_code == 200:
            print("✅ Connection successful!")
            return True
        else:
            print(f"❌ Connection failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error connecting to OpenRouter API: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_chat_completion():
    """Test a simple chat completion request"""
    load_dotenv()
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        print("❌ ERROR: OPENROUTER_API_KEY not found")
        return False
    
    try:
        print("\nTesting chat completion API...")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "Hello World Agent Debug"
        }
        
        # Simple test message
        payload = {
            "model": "anthropic/claude-3-haiku-20240307",  # Use a smaller model for testing
            "messages": [
                {"role": "user", "content": "Hello, are you working properly? Please respond with a very short message."}
            ],
            "temperature": 0.7
        }
        
        response = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30.0
        )
        
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text[:500]}")  # Show truncated response
        
        if response.status_code == 200:
            print("✅ Chat completion successful!")
            return True
        else:
            print(f"❌ Chat completion failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing chat completion: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🔍 OpenRouter API Connection Test 🔍")
    print("===================================")
    
    # Test the API connection
    connection_ok = test_openrouter_connection()
    
    if connection_ok:
        # If connection is successful, test a chat completion
        test_chat_completion()
    
    print("\nTest completed.")