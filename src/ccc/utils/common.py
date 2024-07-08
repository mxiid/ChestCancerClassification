import os
from box.exceptions import BoxValueError
import yaml
from ccc import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): Path like input
    
    Raises:
        ValueError: if YAML file is empty
        e: Empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """creates list of directories

    Args:
        path_to_directories (list): list of directories
        ignore_log (bool, optional): Ignore log. Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """saves json data

    Args: 
        path (Path): path to json file
        data (dict): data to be saved in json file
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"Saved data to: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    
    Args:
        path (Path): path to json file
    
    Returns:
        ConfigBox: ConfigBox type
    """

    with open(path) as f:
        data = json.load(f)

    logger.info(f"Loaded data from: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin (data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved
        path (Path): path to save binary file
    """

    joblib.dump(vale=data, filename=path)
    logger.info(f"Saved binary file at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary file

    Args:
        path (Path): path to binary file
    
    Returns:
        Any: data
    """

    data = joblib.load(path)
    logger.info(f"Loaded binary file from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get file size in KB

    Args:
        path (Path): path to file

    Returns:
        str: file size in KB
    """
    
    size = round(os.path.getsize(path) / 1024)
    return f"~{size} KB"

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as img_file:
        return base64.b64encode(img_file.read())

def decodeImage(imgstring, fileName):
    imgdata=base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

