#!/usr/bin/env python3
"""
Wrapper script for the tester command to work with uv run.
"""
import sys
import os

def main():
    # Add the project root and venv packages to Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)
    venv_packages = os.path.join(project_root, '.venv', 'lib', 'python3.13', 'site-packages')
    sys.path.insert(0, venv_packages)
    
    # Change to project directory
    os.chdir(project_root)
    
    # Import and use the tester functionality
    from tester import run
    
    # Call the run function
    run()

if __name__ == "__main__":
    main()
