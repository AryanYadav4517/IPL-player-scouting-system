import pandas as pd
import matplotlib.pyplot as plt

# Load scouting ranking data
df = pd.read_csv("../data/player_scouting_ranking.csv")

print("🏏 IPL SCOUTING VISUALIZATION")
print("=" * 70)

print("Total players:", len(df))


# ==========================================
# 1. TOP 10 PLAYERS BY SCOUTING SCORE
# ==========================================

top_score = df.sort_values(
    "scouting_score",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_score["player"],
    top_score["scouting_score"]
)

plt.title("Top 10 IPL Players by Scouting Score")
plt.xlabel("Player")
plt.ylabel("Scouting Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 2. TOP 10 RUN SCORERS
# ==========================================

top_runs = df.sort_values(
    "runs",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_runs["player"],
    top_runs["runs"]
)

plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Player")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 3. TOP 10 STRIKE RATES
# ==========================================

top_strike_rate = df.sort_values(
    "strike_rate",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_strike_rate["player"],
    top_strike_rate["strike_rate"]
)

plt.title("Top 10 IPL Players by Strike Rate")
plt.xlabel("Player")
plt.ylabel("Strike Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 4. TOP 10 BOUNDARY PERCENTAGES
# ==========================================

top_boundary = df.sort_values(
    "boundary_percentage",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_boundary["player"],
    top_boundary["boundary_percentage"]
)

plt.title("Top 10 Players by Boundary Percentage")
plt.xlabel("Player")
plt.ylabel("Boundary Percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 5. PLAYER CATEGORY DISTRIBUTION
# ==========================================

category_counts = df["player_category"].value_counts()

plt.figure(figsize=(8, 6))

plt.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct="%1.1f%%"
)

plt.title("IPL Player Category Distribution")
plt.tight_layout()
plt.show()


print("\n✅ All visualizations generated successfully!")
