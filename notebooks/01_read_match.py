import json
import os
import pandas as pd

data_folder = "../data/raw"

all_stats = []

# Go through every JSON file
for filename in os.listdir(data_folder):

    if not filename.endswith(".json"):
        continue

    file_path = os.path.join(data_folder, filename)

    with open(file_path, "r") as file:
        match = json.load(file)

    info = match["info"]

    season = info.get("season")
    date = info["dates"][0]
    venue = info.get("venue", "Unknown")

    teams = list(info["teams"])

    # Process each innings
    for innings in match["innings"]:

        batting_team = innings["team"]

        # Find opponent
        opponent = [team for team in teams if team != batting_team][0]

        player_stats = {}

        for over in innings["overs"]:

            for delivery in over["deliveries"]:

                batter = delivery["batter"]
                runs = delivery["runs"]

                if batter not in player_stats:
                    player_stats[batter] = {
                        "runs": 0,
                        "balls": 0,
                        "fours": 0,
                        "sixes": 0
                    }

                # Batter runs
                player_stats[batter]["runs"] += runs["batter"]

                # Legal delivery = ball faced
                extras = delivery.get("extras", {})

                if "wides" not in extras and "noballs" not in extras:
                    player_stats[batter]["balls"] += 1

                # Boundaries
                if runs["batter"] == 4:
                    player_stats[batter]["fours"] += 1

                if runs["batter"] == 6:
                    player_stats[batter]["sixes"] += 1

        # Store player statistics
        for player, stats in player_stats.items():

            balls = stats["balls"]

            if balls > 0:
                strike_rate = (stats["runs"] / balls) * 100
            else:
                strike_rate = 0
            match_id=filename.replace(".json", "")    
            all_stats.append({
                "match_id":match_id,
                "season": season,
                "date": date,
                "venue": venue,
                "team": batting_team,
                "opponent": opponent,
                "player": player,
                "runs": stats["runs"],
                "balls": balls,
                "fours": stats["fours"],
                "sixes": stats["sixes"],
                "strike_rate": round(strike_rate, 2)
            })


# Convert to DataFrame
df = pd.DataFrame(all_stats)

# Save the dataset
output_file = "../data/player_match_batting.csv"

df.to_csv(output_file, index=False)

print("Processing complete!")
print("Total records:", len(df))
print("\nFirst 10 records:")
print(df.head(10))
