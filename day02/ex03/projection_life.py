from load_csv import load
import sys
import matplotlib.pyplot as plt
import pandas as pd


def clean_value(pop_str: str) -> float | None:
    """
    Convert the values from "5.6M" format to floats
    """
    pop_str = str(pop_str).strip()
    if pop_str.endswith('M'):
        return float(pop_str) * 1_000_000
    elif pop_str.endswith('k'):
        return float(pop_str) * 1_000
    elif pop_str.endswith('B'):
        return float(pop_str) * 1_000_000_000
    try:
        return float(pop_str)
    except ValueError:
        return None


def main():
    """
    Main function to load income and life expectancy data,
    and plot their relationship for the year 1900.
    """
    try:
        life_expectancy_data = load("life_expectancy_years.csv")
        gdp_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if life_expectancy_data is None or gdp_data is None:
            raise AssertionError("Failed to load data")
        if not isinstance(life_expectancy_data, pd.DataFrame) or not \
                isinstance(gdp_data, pd.DataFrame):
            raise AssertionError("Loaded data is not in the \
                                 expected format (DataFrame)")

        life_expectancy_data.set_index("country")
        gdp_data.set_index("country")

        gdp_1900_raw = gdp_data["1900"]
        life_exp_1900_raw = life_expectancy_data["1900"]
        gdp_1900 = gdp_1900_raw.apply(clean_value)
        life_exp_1900 = pd.to_numeric(life_exp_1900_raw, errors="coerce")

        combined_data = pd.DataFrame({'Gdp': gdp_1900,
                                      'Life Expectancy': life_exp_1900})
        combined_data = combined_data.dropna()

        plt.scatter(combined_data['Gdp'], combined_data['Life Expectancy'])
        plt.xscale('log')
        tick_values = [300, 1000, 10000]
        tick_labels = ["300", "1k", "10k"]
        plt.xticks(tick_values, tick_labels)
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
