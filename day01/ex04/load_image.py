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

        with Image.open(path) as img:
            if not img.format or img.format != "JPEG":
                raise AssertionError(f"Error: Invalid image format. "
                                     f"Expected \"JPEG\", got {img.format}")
            pixel_data = np.array(img)
            print(f"The shape of image is: {pixel_data.shape}")
            return pixel_data

    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except IsADirectoryError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except TypeError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}",
              file=sys.stderr)
        sys.exit(1)
