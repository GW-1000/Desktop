import pickle
import re
import os
import pandas as pd
from markets import markets_list
from fuzzywuzzy import fuzz


def matching(events):
    def preprocess(name):
        return re.sub(r'[^\w\s]', '', name)

    avoid_doubles = []
    perma_df = pd.DataFrame({"markets": markets_list})
    for counter1, home1 in enumerate(events.iloc[2, 1:], start=1):
        if counter1 in avoid_doubles:
            continue

        temporary_df = pd.DataFrame({"0": events.iloc[:, counter1]})
        for counter2, home2 in enumerate(events.iloc[2, 1:], start=1):
            if counter1 != counter2 and counter1 not in avoid_doubles:
                if (fuzz.ratio(preprocess(str(home1)), preprocess(str(home2))) >= 65 and
                    fuzz.ratio(preprocess(str(events.iloc[3, counter1])),
                               preprocess(str(events.iloc[3, counter2]))) >= 65
                ) and events.iloc[1, counter1] == events.iloc[1, counter2]:
                    avoid_doubles.extend([counter1, counter2])
                    temporary_df[temporary_df.shape[1]] = events.iloc[:, counter2]

        if temporary_df.shape[1] > 1:
            holding_column = temporary_df.iloc[:, 0].copy()
            # Iterate over each row
            for row_idx, row in temporary_df[4:].iterrows():
                # Extract the second elements of the lists, handling empty lists
                values = [x[1] for x in row if len(x) > 1]
                if values:  # Check if there are any valid values
                    # Find the maximum value
                    max_value = max(values)
                    # Find the index of the maximum value
                    max_idx = [i for i, x in enumerate(row) if len(x) > 1 and x[1] == max_value][0]
                    holding_column.at[row_idx] = temporary_df.iloc[row_idx, max_idx]
                else:
                    holding_column.at[row_idx] = []
            perma_df[perma_df.shape[1]] = holding_column

    return perma_df


# Function to merge DataFrames
def merge_matches(dataframes):
    df1 = dataframes[0]
    for dataframe in dataframes[1:]:
        df = dataframe.drop(dataframe.columns[0], axis=1)
        df1 = pd.concat([df1, df], axis=1)
    return df1


# List to store DataFrames
itz = []

# Path to your folder containing JSON files
folder_path = '/haiti_python/webresults'

# List all files in the folder
files = os.listdir(folder_path)

# Load DataFrames from pickle files
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    # Unpickling the DataFrame
    with open(file_path, 'rb') as file:
        loaded_df = pickle.load(file)
    itz.append(loaded_df)

# Merge DataFrames
file = merge_matches(itz)

# Find common matches and update permanent DataFrame
final_df = matching(file)

# Save merged DataFrame to CSV
final_df.to_csv('merged.csv', index=False)
final_df.to_pickle('merged.pkl')






