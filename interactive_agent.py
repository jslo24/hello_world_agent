"""
Interactive Agent - Modified version of Hello World Agent that supports multiple queries
"""
import os
import sys
import asyncio
from agent.crew import HelloWorldCrew

def print_banner():
    """Display welcome banner"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║       INTERACTIVE HELLO WORLD AGENT - MULTI-QUERY EDITION        ║
╚══════════════════════════════════════════════════════════════════╝

Welcome to the Interactive Agent! You can ask multiple questions in a single session.
Type 'exit', 'quit', or 'bye' to end the session.
Type 'help' for more commands.
    """)

def print_help():
    """Display help information"""
    print("""
Available commands:
- 'exit', 'quit', or 'bye': End the session
- 'help': Display this help message
- 'research [query]': Run only the research phase for your query
- 'execute [query]': Run only the execution phase for your query
- 'analyze [query]': Run only the analysis phase for your query
- 'clear': Clear the screen
- Any other input will be processed as a full query (research + execution)
    """)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

async def main():
    """Run the interactive agent"""
    print_banner()
    
    # Initialize the agent
    crew = HelloWorldCrew(enable_hitl=True)
    
    while True:
        try:
            # Get user input
            print("\n\033[1;36m💬 What would you like me to help you with?\033[0m")
            user_input = input("> ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n\033[1;33m👋 Goodbye! Thank you for using the Interactive Agent.\033[0m")
                break
                
            # Check for help command
            elif user_input.lower() == 'help':
                print_help()
                continue
                
            # Check for clear command
            elif user_input.lower() == 'clear':
                clear_screen()
                print_banner()
                continue
                
            # Check for specific phase commands
            elif user_input.lower().startswith('research '):
                query = user_input[9:].strip()
                if query:
                    await crew.run_with_streaming(prompt=query, task_type="research")
                else:
                    print("\033[1;31mPlease provide a query after 'research'\033[0m")
                    
            elif user_input.lower().startswith('execute '):
                query = user_input[8:].strip()
                if query:
                    await crew.run_with_streaming(prompt=query, task_type="execute")
                else:
                    print("\033[1;31mPlease provide a query after 'execute'\033[0m")
                    
            elif user_input.lower().startswith('analyze '):
                query = user_input[8:].strip()
                if query:
                    await crew.run_with_streaming(prompt=query, task_type="analyze")
                else:
                    print("\033[1;31mPlease provide a query after 'analyze'\033[0m")
                    
            # Process as a regular query
            elif user_input:
                print(f"\n\033[1;32m🔍 Processing: {user_input}\033[0m\n")
                await crew.run_with_streaming(prompt=user_input, task_type="both")
                print("\n\033[1;32m✅ Query processing complete\033[0m")
                
            else:
                print("\033[1;31mPlease enter a query or command\033[0m")
                
        except KeyboardInterrupt:
            print("\n\033[1;33m⚠️ Operation interrupted\033[0m")
            continue
            
        except Exception as e:
            print(f"\n\033[1;31m❌ Error: {str(e)}\033[0m")
            print("Try a different query or restart the agent if issues persist.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\033[1;33m👋 Goodbye! Thank you for using the Interactive Agent.\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m❌ Critical error: {str(e)}\033[0m")