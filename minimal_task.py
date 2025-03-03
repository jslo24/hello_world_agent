"""
Minimal task script that avoids using the crew directly
"""
import os
import sys
import importlib.util

# Ensure current directory is in path
sys.path.insert(0, os.getcwd())

def main():
    try:
        print("\n🔍 ANALYZING REPOSITORY STRUCTURE\n")
        
        # Try to load main.py directly
        main_path = os.path.join('agent', 'main.py')
        if os.path.exists(main_path):
            print(f"Found {main_path}, attempting to run it directly")
            
            # Load main.py as a module
            spec = importlib.util.spec_from_file_location("agent_main", main_path)
            agent_main = importlib.util.module_from_spec(spec)
            
            # This actually executes the module
            spec.loader.exec_module(agent_main)
            
            # If main has a main() function, call it
            if hasattr(agent_main, 'main'):
                print("Calling main() function")
                agent_main.main()
            else:
                print("Module loaded but no main() function found")
                
        else:
            print(f"Could not find {main_path}")
            
    except Exception as e:
        import traceback
        print(f"Error occurred: {e}")
        traceback.print_exc()
        
        # Print additional debugging info
        print("\nFiles in agent directory:")
        if os.path.exists('agent'):
            for item in os.listdir('agent'):
                print(f" - {item}")
                
        print("\nContent of agent/crew.py:")
        crew_path = os.path.join('agent', 'crew.py')
        if os.path.exists(crew_path):
            with open(crew_path, 'r') as f:
                print(f.read())

if __name__ == "__main__":
    main()