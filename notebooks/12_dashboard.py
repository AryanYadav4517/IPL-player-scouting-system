import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# IPL PLAYER SCOUTING DASHBOARD
# ==========================================

# Load scouting ranking dataset
scouting = pd.read_csv("../data/player_scouting_ranking.csv")

print("🏏 IPL PLAYER SCOUTING DASHBOARD")
print("=" * 70)

print("\nTotal players available:", len(scouting))

# ==========================================
# TOP 10 PLAYERS
# ==========================================

top10 = scouting.sort_values(
    "scouting_score",
    ascending=False
).head(10)

print("\nTOP 10 PLAYERS")
print("=" * 70)

print(
    top10[
        [
            "rank",
            "player",
            "runs",
            "strike_rate",
            "boundary_percentage",
            "scouting_score"
        ]
    ].to_string(index=False)
)

# ==========================================
# TOP 10 SCOUTING SCORE CHART
# ==========================================

plt.figure(figsize=(12, 6))

plt.bar(
    top10["player"],
    top10["scouting_score"]
)

plt.title("Top 10 IPL Players by Scouting Score")
plt.xlabel("Player")
plt.ylabel("Scouting Score")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()

# ==========================================
# STRIKE RATE vs RUNS
# ==========================================

plt.figure(figsize=(10, 6))

plt.scatter(
    scouting["runs"],
    scouting["strike_rate"]
)

plt.title("IPL Players: Runs vs Strike Rate")
plt.xlabel("Total Runs")
plt.ylabel("Strike Rate")

plt.tight_layout()
plt.show()

# ==========================================
# PLAYER CATEGORY DISTRIBUTION
# ==========================================

def categorize_player(row):

    if row["strike_rate"] >= 145:
        return "Aggressive Batter"

    elif row["matches"] >= 180 and row["runs"] >= 5000:
        return "Experienced Performer"

    elif row["runs_per_match"] >= 35:
        return "Consistent Performer"

    else:
        return "Developing Player"


scouting["player_category"] = scouting.apply(
    categorize_player,
    axis=1
)

print("\nPLAYER CATEGORY DISTRIBUTION")
print("=" * 70)

print(
    scouting["player_category"]
    .value_counts()
)

# ==========================================
# CATEGORY PIE CHART
# ==========================================

category_counts = scouting["player_category"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("IPL Player Category Distribution")

plt.tight_layout()
plt.show()

# ==========================================
# SAVE DASHBOARD DATA
# ==========================================

scouting.to_csv(
    "../data/final_player_scouting.csv",
    index=False
)

print("\n✅ Dashboard data saved successfully!")

print("\n🎯 IPL SCOUTING DASHBOARD COMPLETED!")


# ==========================================
# PLAYER COMPARISON
# ==========================================

print("\n")
print("PLAYER COMPARISON")
print("=" * 70)

player1 = "V Kohli"
player2 = "RG Sharma"

p1 = scouting[scouting["player"] == player1].iloc[0]
p2 = scouting[scouting["player"] == player2].iloc[0]

print("\nMetric              ", player1, "     ", player2)
print("-" * 70)

print("Runs                 ", p1["runs"], "        ", p2["runs"])
print("Strike Rate         ", p1["strike_rate"], "     ", p2["strike_rate"])
print("Boundary %          ", p1["boundary_percentage"], "     ", p2["boundary_percentage"])
print("Scouting Score      ", p1["scouting_score"], "     ", p2["scouting_score"])

print("\n🏆 SCOUTING RECOMMENDATION")
print("=" * 70)

if p1["scouting_score"] > p2["scouting_score"]:
    print(player1, "is recommended based on the higher scouting score.")
else:
    print(player2, "is recommended based on the higher scouting score.")
