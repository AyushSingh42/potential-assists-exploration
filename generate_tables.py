import great_tables as gt
import gt_extras as gte
import pandas as pd

df = pd.read_csv("potential_assists_leaderboard.csv")

df_sorted = df.sort_values(by="AST_CONVERSION_RATE", ascending=False)
top_10 = df_sorted.head(10)
bottom_10 = df_sorted.tail(10)

img_paths = "https://raw.githubusercontent.com/Henryjean/data/refs/heads/main/square_nba_logos/"

table_top = (
    gt.GT(top_10)
    .tab_header(title=gt.md("**Top 10 Potential Assist Conversion Rates**"))
    .cols_hide(columns=["TOTAL_pAST"])
    .cols_label({
        "TEAM_ABBREVIATION": "",
        "PLAYER_NAME": "PLAYER",
        "AST": "AST",
        "POTENTIAL_AST": "pAST",
        "AST_CONVERSION_RATE": "ASR"
    })
    .fmt_number(columns="AST_CONVERSION_RATE", decimals=3)
    .fmt_image(columns="TEAM_ABBREVIATION", path=img_paths, file_pattern="{}.svg")
    .cols_align(columns=["AST", "pAST", "ASR"], align="right")
)

table_top.save("top_10_asr.png", scale=3, expand=20)

table_bottom = (
    gt.GT(bottom_10)
    .tab_header(title=gt.md("**Bottom 10 Potential Assist Conversion Rates**"))
    .cols_hide(columns=["TOTAL_pAST"])
    .cols_label({
        "TEAM_ABBREVIATION": "",
        "PLAYER_NAME": "PLAYER",
        "AST": "AST",
        "POTENTIAL_AST": "pAST",
        "AST_CONVERSION_RATE": "ASR"
    })
    .fmt_number(columns="AST_CONVERSION_RATE", decimals=3)
    .fmt_image(columns="TEAM_ABBREVIATION", path=img_paths, file_pattern="{}.svg")
    .cols_align(columns=["AST", "pAST", "ASR"], align="right")
)

table_bottom.save("bottom_10_asr.png", scale=3, expand=20)