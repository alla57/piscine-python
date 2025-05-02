import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd
import sys
import matplotlib.ticker as ticker


def format_population(value, pos):
    """
    Formatter function for y-axis ticks to display large numbers concisely.
    Example: 20,000,000 -> '20M'
             500,000   -> '500k'
    """
    if value >= 1_000_000_000:
        return f'{value / 1_000_000_000:.0f}B'
    if value >= 1_000_000:
        return f'{value / 1_000_000:.0f}M'
    if value >= 1_000:
        return f'{value / 1_000:.0f}k'
    return f'{value:.0f}'


def clean_population(pop_str):
    """
    Convert the values from "5.6M" format to floats
    """
    pop_str = str(pop_str).strip().replace(',', '')
    if pop_str.endswith('M'):
        return float(pop_str[:-1]) * 1_000_000
    elif pop_str.endswith('k'):
        return float(pop_str[:-1]) * 1_000
    elif pop_str.endswith('B'):
        return float(pop_str[:-1]) * 1_000_000_000
    try:
        return float(pop_str)
    except ValueError:
        return None


def main():
    """
    Main function to load data, filter for the campus countries,
    and compare total population.
    """
    try:
        file_path = "population_total.csv"
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
        population_cleaned = country_series.apply(clean_population)
        population = population_cleaned.values
        plt.plot(years, population, label=f'{campus_country}')

        campus_country2 = "Belgium"
        country_series2 = data.loc[campus_country2]
        years2 = country_series2.index.astype(int)
        population_cleaned2 = country_series2.apply(clean_population)
        population2 = population_cleaned2.values
        plt.plot(years2, population2, label=f'{campus_country2}')

        ax = plt.gca()
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_population))

        year_start = 1800
        year_end = 2050
        plt.title(f"{campus_country} Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc='lower right')
        plt.xlim(year_start, year_end)
        plt.xticks(range(year_start, year_end + 1, 40))
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
