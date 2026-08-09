import pandas as pd

# Load scouting ranking data
df = pd.read_csv("../data/player_scouting_ranking.csv")

print("IPL PLAYER RECOMMENDATION SYSTEM")
print("=" * 70)

# Display available categories
print("\nAvailable Player Categories:")
print(df["player_category"].value_counts())

# ==========================================
# RECOMMENDATION FUNCTION
# ==========================================

def recommend_players(category, top_n=5):

    result = df[
        df["player_category"].str.lower() == category.lower()
    ].copy()

    result = result.sort_values(
        "scouting_score",
        ascending=False
    )

    return result[
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
    ].head(top_n)


# ==========================================
# EXAMPLE RECOMMENDATIONS
# ==========================================

print("\nTOP AGGRESSIVE BATTERS")
print("=" * 70)

print(
    recommend_players(
        "Aggressive Batter",
        5
    ).to_string(index=False)
)


print("\nTOP CONSISTENT PERFORMERS")
print("=" * 70)

print(
    recommend_players(
        "Consistent Performer",
        5
    ).to_string(index=False)
)


print("\nTOP EXPERIENCED PERFORMERS")
print("=" * 70)

print(
    recommend_players(
        "Experienced Performer",
        5
    ).to_string(index=False)
)
