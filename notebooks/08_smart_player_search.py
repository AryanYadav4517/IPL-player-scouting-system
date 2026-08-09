import pandas as pd

# Load scouting ranking data
df = pd.read_csv("../data/player_scouting_ranking.csv")

print("🏏 IPL SMART PLAYER SCOUTING SYSTEM")
print("=" * 70)

# Show basic information
print("\nTotal players available:", len(df))

# ==========================================
# SMART SEARCH FUNCTION
# ==========================================

def search_players(min_runs=0, min_strike_rate=0,
                    min_boundary_percentage=0,
                    min_matches=0, top_n=10):

    result = df[
        (df["runs"] >= min_runs) &
        (df["strike_rate"] >= min_strike_rate) &
        (df["boundary_percentage"] >= min_boundary_percentage) &
        (df["matches"] >= min_matches)
    ].copy()

    # Sort by scouting score
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
# EXAMPLE 1
# ==========================================

print("\n🔥 HIGH STRIKE-RATE BATTERS")
print("=" * 70)

print(
    search_players(
        min_strike_rate=140,
        top_n=5
    ).to_string(index=False)
)


# ==========================================
# EXAMPLE 2
# ==========================================

print("\n💥 HIGH RUN SCORERS")
print("=" * 70)

print(
    search_players(
        min_runs=5000,
        top_n=5
    ).to_string(index=False)
)


# ==========================================
# EXAMPLE 3
# ==========================================

print("\n🎯 POWER HITTERS")
print("=" * 70)

print(
    search_players(
        min_strike_rate=145,
        min_boundary_percentage=65,
        top_n=5
    ).to_string(index=False)
)


# ==========================================
# EXAMPLE 4
# ==========================================

print("\n🏆 EXPERIENCED HIGH-PERFORMERS")
print("=" * 70)

print(
    search_players(
        min_runs=4000,
        min_strike_rate=130,
        min_matches=100,
        top_n=5
    ).to_string(index=False)
)
