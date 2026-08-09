import pandas as pd

# Load match-level batting data
df = pd.read_csv("../data/player_match_batting.csv")

# Create player-level statistics
scouting = df.groupby("player").agg(
    matches=("match_id", "nunique"),
    runs=("runs", "sum"),
    balls=("balls", "sum"),
    fours=("fours", "sum"),
    sixes=("sixes", "sum")
).reset_index()

# Calculate runs per match
# Total runs / number of matches
scouting["runs_per_match"] = (
    scouting["runs"] / scouting["matches"]
).round(2)

# Calculate overall strike rate
scouting["strike_rate"] = (
    scouting["runs"] / scouting["balls"] * 100
).round(2)

# Calculate boundary percentage
scouting["boundary_runs"] = (
    scouting["fours"] * 4 +
    scouting["sixes"] * 6
)

scouting["boundary_percentage"] = (
    scouting["boundary_runs"] /
    scouting["runs"] * 100
).round(2)
# Remove players with very small sample sizes
# Minimum 200 balls faced
scouting = scouting[scouting["balls"] >= 200].copy()

# Sort by total runs
scouting = scouting.sort_values(
    "runs",
    ascending=False
)

print("PLAYER SCOUTING DATASET")
print("=" * 70)

print(scouting.head(20).to_string(index=False))

print("\nTotal players:", len(scouting))

# Save player-level dataset
scouting.to_csv(
    "../data/player_scouting.csv",
    index=False
)

print("\nScouting dataset saved successfully!")

# ==============================
# SCOUTING SCORE
# ==============================

# Normalize important metrics to a 0-100 scale

scouting["run_score"] = (
    scouting["runs"] / scouting["runs"].max() * 100
)

scouting["strike_rate_score"] = (
    scouting["strike_rate"] /
    scouting["strike_rate"].max() * 100
)

scouting["runs_per_match_score"] = (
    scouting["runs_per_match"] /
    scouting["runs_per_match"].max() * 100
)

scouting["boundary_score"] = (
    scouting["boundary_percentage"] /
    scouting["boundary_percentage"].max() * 100
)

# Experience score
scouting["experience_score"] = (
    scouting["matches"] /
    scouting["matches"].max() * 100
)

# Final scouting score
# Runs = 35%
# Strike Rate = 25%
# Runs per Match = 20%
# Boundary Percentage = 10%
# Experience = 10%

scouting["scouting_score"] = (
    scouting["run_score"] * 0.35 +
    scouting["strike_rate_score"] * 0.25 +
    scouting["runs_per_match_score"] * 0.20 +
    scouting["boundary_score"] * 0.10 +
    scouting["experience_score"] * 0.10
).round(2)

# ==============================
# PLAYER CLASSIFICATION
# ==============================

def classify_player(row):

    # High scoring + good consistency
    if row["scouting_score"] >= 65 and row["runs_per_match"] >= 30:
        return "Consistent Performer"

    # Very aggressive batting style
    elif row["strike_rate"] >= 145 and row["boundary_percentage"] >= 60:
        return "Aggressive Batter"

    # Good performance with less experience
    elif row["matches"] <= 50 and row["scouting_score"] >= 45:
        return "Emerging Player"

    # Experienced player with solid performance
    elif row["matches"] >= 100 and row["scouting_score"] >= 45:
        return "Experienced Performer"

    else:
        return "Developing Player"


scouting["player_category"] = scouting.apply(
    classify_player,
    axis=1
)

# Remove invalid values before ranking

scouting["scouting_score"] = (
    scouting["scouting_score"]
    .replace([float("inf"), float("-inf")], 0)
    .fillna(0)
)

# Rank players
scouting["rank"] = (
    scouting["scouting_score"]
    .rank(method="min", ascending=False)
    .astype(int)

)

# Sort by scouting score
scouting = scouting.sort_values(
    "scouting_score",
    ascending=False
)

print("\n")
print("IPL PLAYER SCOUTING RANKING")
print("=" * 80)

print(
    scouting[
        [
            "rank",
            "player",
            "matches",
            "runs",
            "strike_rate",
            "boundary_percentage",
            "scouting_score",
            "player_category"
        ]
    ].head(20).to_string(index=False)
)

# Save final scouting ranking
scouting.to_csv(
    "../data/player_scouting_ranking.csv",
    index=False
)

print("\nScouting ranking saved successfully!")
