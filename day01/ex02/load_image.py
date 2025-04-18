import numpy as np
from PIL import Image
import sys
import os


def ft_load(path: str) -> np.ndarray | None:
    try:
        if not isinstance(path, str):
            raise AssertionError("Error the provided path is not a string")
        if not os.path.exists(path):
            raise FileNotFoundError("Error the path doesn't exist")
        if not os.path.isfile(path):
            raise IsADirectoryError("Error the given path is not a file")
        if not os.access(path, os.R_OK):
            raise PermissionError(f"Error No permission for file: {path}")
        