import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")
        return None
