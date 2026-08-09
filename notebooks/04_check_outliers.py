import pandas as pd

df = pd.read_csv("../data/player_match_batting.csv")

# Show highest strike rates
top_sr = df.sort_values("strike_rate", ascending=False)

print("TOP 20 STRIKE RATES")
print("-" * 70)

print(
    top_sr[
        ["season", "player", "runs", "balls", "fours", "sixes", "strike_rate"]
    ].head(20).to_string(index=False)
)

# Find players with very few balls
print("\n\nHIGH STRIKE RATE WITH 1-2 BALLS")
print("-" * 70)

small_sample = df[
    (df["balls"] <= 2) &
    (df["strike_rate"] >= 300)
]

print(
    small_sample[
        ["season", "player", "runs", "balls", "fours", "sixes", "strike_rate"]
    ].head(30).to_string(index=False)
)
