import pandas as pd

df = pd.read_csv("../data/player_match_batting.csv")

# Aggregate career IPL batting statistics
players = df.groupby("player").agg(
    runs=("runs", "sum"),
    balls=("balls", "sum"),
    fours=("fours", "sum"),
    sixes=("sixes", "sum"),
    matches=("date", "nunique")
).reset_index()

# Calculate overall strike rate
players["strike_rate"] = (
    players["runs"] / players["balls"] * 100
)

# Only players with a meaningful batting sample
qualified = players[players["balls"] >= 500].copy()

# Top 20 by runs
top_runs = qualified.sort_values("runs", ascending=False).head(20)

print("TOP 20 IPL BATTERS BY RUNS")
print("-" * 80)

print(
    top_runs[
        ["player", "matches", "runs", "balls", "fours", "sixes", "strike_rate"]
    ].to_string(index=False)
)
