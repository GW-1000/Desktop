import pickle
from comparison_temp import compare
import pandas
import pandas as pd

# Unpickling the DataFrame
with open('merged.pkl', 'rb') as file:
    loaded_df: pandas.DataFrame = pickle.load(file)

# Function to calculate arbitrage
def calculate_arbitrage(odds1, odds2):
    try:
        arbitrage_percentage = (1 / float(odds1[1])) + (1 / float(odds2[1]))
        arbitrage_percentage = (1 - arbitrage_percentage) * 100
    except ZeroDivisionError:
        return 0
    return arbitrage_percentage


# Pre-written list of comparisons
my_comparisons = compare

# Iterate through comparisons
for base_market, compare_market in my_comparisons:
    # Get the rows corresponding to the base and compare markets
    base_row = loaded_df[loaded_df['markets'] == base_market]
    compare_row = loaded_df[loaded_df['markets'] == compare_market]

    if not base_row.empty and not compare_row.empty:
        # Iterate over the odds columns directly
        for col in loaded_df.columns[1:]:  # Skip the first column ('Market')
            odds1 = base_row[col].values[0]
            odds2 = compare_row[col].values[0]
            if odds1 and odds2:
                arb_opportunity = calculate_arbitrage(odds1, odds2)
                if arb_opportunity > 0:
                    # Print the comparison result
                    print(arb_opportunity)
                    print(f"{loaded_df.iloc[2, col]} VS {loaded_df.iloc[3, col]}")
                    print(f"Comparing {base_market} to {compare_market}")
                    print(f"Odds for {base_market} in {col}: {odds1}")
                    print(f"Odds for {compare_market} in {col}: {odds2}")




