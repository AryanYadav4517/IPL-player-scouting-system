import pandas as pd

# Load scouting ranking data
df = pd.read_csv("../data/player_scouting_ranking.csv")

print("🏏 IPL PLAYER COMPARISON SYSTEM")
print("=" * 75)

print("\nTotal players available:", len(df))


# ==========================================
# PLAYER COMPARISON FUNCTION
# ==========================================

def compare_players(player1, player2):

    p1 = df[df["player"].str.lower() == player1.lower()]
    p2 = df[df["player"].str.lower() == player2.lower()]

    # Check if players exist
    if p1.empty:
        print("\nPlayer not found:", player1)
        return

    if p2.empty:
        print("\nPlayer not found:", player2)
        return

    p1 = p1.iloc[0]
    p2 = p2.iloc[0]

    comparison = pd.DataFrame({
        "Metric": [
            "Matches",
            "Runs",
            "Strike Rate",
            "Boundary Percentage",
            "Scouting Score"
        ],

        player1: [
            p1["matches"],
            p1["runs"],
            p1["strike_rate"],
            p1["boundary_percentage"],
            p1["scouting_score"]
        ],

        player2: [
            p2["matches"],
            p2["runs"],
            p2["strike_rate"],
            p2["boundary_percentage"],
            p2["scouting_score"]
        ]
    })

    print("\nPLAYER COMPARISON")
    print("=" * 75)

    print(comparison.to_string(index=False))

    # ======================================
    # SCOUTING SCORE WINNER
    # ======================================

    print("\n🏆 SCOUTING RECOMMENDATION")
    print("=" * 75)

    if p1["scouting_score"] > p2["scouting_score"]:

        print(
            f"{player1} is recommended based on the higher "
            f"scouting score."
        )

    elif p2["scouting_score"] > p1["scouting_score"]:

        print(
            f"{player2} is recommended based on the higher "
            f"scouting score."
        )

    else:

        print("Both players have the same scouting score.")


# ==========================================
# COMPARISON 1
# ==========================================

compare_players(
    "V Kohli",
    "RG Sharma"
)


# ==========================================
# COMPARISON 2
# ==========================================

compare_players(
    "CH Gayle",
    "AB de Villiers"
)
