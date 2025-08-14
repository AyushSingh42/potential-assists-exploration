from nba_api.stats.endpoints import LeagueDashPtStats
import pandas as pd

# Fetch player-level passing stats for 2024-25 season
stats = LeagueDashPtStats(
    pt_measure_type="Passing",
    season="2024-25",
    per_mode_simple="PerGame",
    player_or_team="Player"  # <-- important
)

df = stats.get_data_frames()[0]

# Now you should have PLAYER_NAME column
print(df.columns)

# Select relevant columns
df = df[["PLAYER_NAME", "TEAM_ABBREVIATION", "GP", "AST", "POTENTIAL_AST"]]
df["AST_CONVERSION_RATE"] = (df["AST"] / df["POTENTIAL_AST"]).round(3)

print(df.head(10))
df.to_csv("potential_assists.csv", index=False)
 