import pandas as pd

file_path = "../data/player_match_batting.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn names:")
print(df.columns.tolist())

print("\nSeasons available:")
print(sorted(df["season"].unique()))

print("\nNumber of unique players:")
print(df["player"].nunique())

print("\nMissing values:")
print(df.isnull().sum())
