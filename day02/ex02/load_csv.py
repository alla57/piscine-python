import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Loads data from a CSV file into a pandas DataFrame.
    Args:
        path (str): The file path to the CSV file to be loaded.

    Returns:
        pd.DataFrame | None: A pandas DataFrame containing the data from the
            CSV file if loading is successful. Returns None if any error
            occurs during the loading process.

    Prints:
        - Success message with DataFrame dimensions upon successful loading.
        - Error message with exception type and details upon failure.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")
        return None
