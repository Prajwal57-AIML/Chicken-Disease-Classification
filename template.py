import os
from pathlib import Path
import logging

# Basic logging configuration so we can track what the script is creating
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# This will be the root package name for our CNN project
# Keeping it lowercase and without spaces for best practice
project_name = "cnnClassifier"

# List of all files and directories we want to auto-generate
# This helps in setting up a clean and modular project structure quickly
list_of_files = [
    ".github/workflows/.gitkeep",  # Keeps GitHub workflow directory tracked
    
    # Core source package structure
    f"src/{project_name}/__init__.py",  # Makes this directory a Python package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  # Configuration management
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    # Configuration and experiment tracking files
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",

    # Project-level setup files
    "requirements.txt",
    "setup.py",

    # Research and frontend placeholders
    "research/trials.ipynb",
    "templates/index.html"
]

# Looping through each file path to create directories and empty files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it does not already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Create empty file only if it does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Just creating an empty placeholder file
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
