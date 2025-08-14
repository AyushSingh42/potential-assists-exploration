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
df = df[[ "TEAM_ABBREVIATION", "PLAYER_NAME", "GP", "AST", "POTENTIAL_AST"]]
df["AST_CONVERSION_RATE"] = (df["AST"] / df["POTENTIAL_AST"]).round(3)

MIN_POTENTIAL_AST = 200  # adjust based on your threshold
df["TOTAL_pAST"] = df["POTENTIAL_AST"] * df ["GP"]
df = df[df["TOTAL_pAST"] >= MIN_POTENTIAL_AST]

df_sorted = df.sort_values(by="POTENTIAL_AST", ascending=False)
df_sorted.to_csv("potential_assists_leaderboard.csv", index=False)