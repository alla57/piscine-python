import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd
import sys


def main():
    """
    Main function to load data, filter for the campus country,
    and plot life expectancy.
    """
    try:
        file_path = "life_expectancy_years.csv"
        data = load(file_path)
        if data is None:
            raise AssertionError("Failed to load data")
        if not isinstance(data, pd.DataFrame):
            raise AssertionError("Loaded data is not in the \
                                 expected format (DataFrame)")

        campus_country = "France"
        data.set_index('country', inplace=True)
        country_series = data.loc[campus_country]
        years = country_series.index.astype(int)
        life_expectancies = country_series.values

        plt.plot(years, life_expectancies)
        plt.title(f"{campus_country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
