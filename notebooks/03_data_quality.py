import pandas as pd

df = pd.read_csv("../data/player_match_batting.csv")

print("Total rows:", len(df))

# Check duplicate rows
duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)

# Check data types
print("\nData types:")
print(df.dtypes)

# Basic statistics
print("\nBasic statistics:")
print(df[["runs", "balls", "fours", "sixes", "strike_rate"]].describe())
