"""
Custom Task for Hello World Agent
"""
import os
import sys

# Make sure our current directory is in the path
sys.path.insert(0, os.getcwd())

def main():
    try:
        # Try importing the crew
        from agent.crew import HelloWorldCrew
        from agent.config.config_loader import load_config
        
        # Load the configuration
        config = load_config()
        
        # Set your custom task here
        custom_task = "Research the latest developments in quantum computing and summarize the key findings."
        
        # Print task information
        print(f"\n🔍 EXECUTING CUSTOM TASK: {custom_task}\n")
        
        # Initialize the crew with your custom task
        crew = HelloWorldCrew(task=custom_task)
        
        # Run the crew with HITL enabled
        result = crew.run(hitl=True)
        
        # Print the result
        print("\n✅ TASK COMPLETED")
        print("\n🔍 RESULTS:")
        print(result)
        
    except Exception as e:
        import traceback
        print(f"Error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()