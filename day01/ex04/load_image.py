import numpy as np
from PIL import Image
import sys
import os


def ft_load(path: str) -> np.ndarray | None:
    """Loads a JPEG image, prints its shape, and returns its pixel data.

    Validates the provided path for existence, file type, and read permissions.
    Checks if the loaded image format is strictly JPEG.
    If all checks pass, it prints the image shape (height, width, channels)
    to standard output and returns the image pixel data as a NumPy array.

    In case of any validation error (path issues, permissions, non-JPEG format)
    or any error during image loading, the function prints a descriptive
    error message to standard error and terminates the program execution
    by calling sys.exit(1).

    Args:
        path (str): The file path to the JPEG image file.

    Returns:
        np.ndarray: A NumPy array containing the image pixel data
        (typically RGB).
                This return only occurs if the image is loaded successfully.
                The function will exit otherwise.

    Prints:
        - "The shape of image is: (height, width, channels)"
        to stdout on success.
        - Error messages to stderr on failure before exiting.

    Raises:
        SystemExit: The function calls sys.exit(1) upon any detected error,
                    effectively raising SystemExit after printing to stderr.
                    Specific errors caught include: AssertionError (for path
                    type or image format), FileNotFoundError,
                    IsADirectoryError,PermissionError, and other general
                    Exceptions during loading.
    """
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
