import pandas as pd

# Load scouting ranking data
df = pd.read_csv("../data/player_scouting_ranking.csv")

print("🏏 IPL TEAM REQUIREMENT ENGINE")
print("=" * 75)

print("\nTotal players available:", len(df))


# ==========================================
# TEAM REQUIREMENT FUNCTION
# ==========================================

def find_players(
    category=None,
    min_runs=0,
    min_strike_rate=0,
    min_matches=0,
    top_n=5
):

    result = df.copy()

    # Filter by player category
    if category:
        result = result[
            result["player_category"].str.lower()
            == category.lower()
        ]

    # Apply performance requirements
    result = result[
        (result["runs"] >= min_runs) &
        (result["strike_rate"] >= min_strike_rate) &
        (result["matches"] >= min_matches)
    ]

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
# REQUIREMENT 1
# ==========================================

print("\n🔥 REQUIREMENT 1")
print("Team needs an Aggressive Batter")
print("=" * 75)

print(
    find_players(
        category="Aggressive Batter",
        top_n=5
    ).to_string(index=False)
)


# ==========================================
# REQUIREMENT 2
# ==========================================

print("\n🎯 REQUIREMENT 2")
print("Team needs an experienced high-run scorer")
print("=" * 75)

print(
    find_players(
        category="Experienced Performer",
        min_runs=4000,
        min_matches=100,
        top_n=5
    ).to_string(index=False)
)


# ==========================================
# REQUIREMENT 3
# ==========================================

print("\n💥 REQUIREMENT 3")
print("Team needs a high strike-rate batter")
print("=" * 75)

print(
    find_players(
        min_strike_rate=145,
        min_runs=2000,
        top_n=5
    ).to_string(index=False)
)


# ==========================================
# REQUIREMENT 4
# ==========================================

print("\n🏆 REQUIREMENT 4")
print("Team needs a reliable top performer")
print("=" * 75)

print(
    find_players(
        min_runs=5000,
        min_strike_rate=130,
        min_matches=150,
        top_n=5
    ).to_string(index=False)
)


print("\n✅ Team requirement analysis completed!")
