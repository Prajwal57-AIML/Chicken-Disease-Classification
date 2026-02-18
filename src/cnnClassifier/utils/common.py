import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


# This function reads a YAML file and converts it into
# a ConfigBox object so we can access values using dot notation.
# Example: config.key instead of config["key"]

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        # Open and load YAML file safely
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            # Logging just to confirm file was loaded
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")

            # Convert dictionary to ConfigBox for easy attribute access
            return ConfigBox(content)

    # If YAML file exists but is empty
    except BoxValueError:
        raise ValueError("yaml file is empty")

    # If anything else goes wrong, raise the actual error
    except Exception as e:
        raise e



# Creates multiple directories if they don’t exist.
# Very useful during project setup.


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):

    for path in path_to_directories:
        # exist_ok=True prevents error if folder already exists
        os.makedirs(path, exist_ok=True)

        # Print log only if verbose is True
        if verbose:
            logger.info(f"created directory at: {path}")



# Save dictionary data into a JSON file.
# Used for storing configuration, metrics, etc.


def save_json(path: Path, data: dict):

    # Write JSON file with indentation for readability
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")



# Load JSON file and convert it into ConfigBox
# so we can access values like object attributes.


def load_json(path: Path) -> ConfigBox:

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")

    return ConfigBox(content)



# Save any Python object in binary format using joblib.
# Commonly used for saving ML models.


@ensure_annotations
def save_bin(data: Any, path: Path):

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")



# Load binary file (like a saved ML model).


@ensure_annotations
def load_bin(path: Path) -> Any:

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")

    return data



# Returns file size in KB (rounded).
# Helpful when checking model file size.


@ensure_annotations
def get_size(path: Path) -> str:

    size_in_kb = round(os.path.getsize(path) / 1024)

    return f"~ {size_in_kb} KB"



# Decode a base64 string and save it as an image file.
# Mostly used in API deployments where image comes as base64.


def decodeImage(imgstring, fileName):

    imgdata = base64.b64decode(imgstring)

    with open(fileName, 'wb') as f:
        f.write(imgdata)



# Convert an image file into base64 format.
# Useful when sending images through APIs.


def encodeImageIntoBase64(croppedImagePath):

    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
