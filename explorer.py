"""
Explorer script to help debug module structure
"""
import os
import sys
import importlib
import pkgutil

def main():
    # Print Python details
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    
    # Print environment variables
    print("\nPYTHONPATH:")
    for path in sys.path:
        print(f" - {path}")
    
    # List all directories and files in current directory
    print("\nFiles in current directory:")
    for item in os.listdir('.'):
        print(f" - {item}")
    
    # Check for specific directories
    if os.path.exists('agent'):
        print("\nFiles in agent directory:")
        for item in os.listdir('agent'):
            print(f" - {item}")
        
        # Check tools directory
        if os.path.exists('agent/tools'):
            print("\nFiles in agent/tools directory:")
            for item in os.listdir('agent/tools'):
                print(f" - {item}")
    
    # Try importing modules
    print("\nTrying imports:")
    modules_to_try = [
        'agent', 
        'agent.crew',
        'agent.tools',
        'agent.config',
        'agent.config.config_loader'
    ]
    
    for module_name in modules_to_try:
        try:
            module = importlib.import_module(module_name)
            print(f" ✓ Successfully imported {module_name}")
        except ImportError as e:
            print(f" ✗ Failed to import {module_name}: {e}")
    
    # List all installed packages
    print("\nInstalled packages:")
    installed_packages = sorted([pkg.name for pkg in pkgutil.iter_modules()])
    print(", ".join(installed_packages[:20]) + "..." if len(installed_packages) > 20 else "")

if __name__ == "__main__":
    main()