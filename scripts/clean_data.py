import pandas as pd


def clean_team_schedule(team, year):
    input_path = f"data/raw/{team}_{year}_games.csv"
    output_path = f"data/processed/{team}_{year}_cleaned.csv"

    games = pd.read_csv(input_path)

    cleaned = games.copy()

    cleaned = cleaned.rename(columns={
        "Gm#": "game_number",
        "Date": "date",
        "Tm": "team",
        "Unnamed: 4": "home_away",
        "Opp": "opponent",
        "W/L": "result",
        "R": "runs_scored",
        "RA": "runs_allowed"
    })

    cleaned["is_home"] = cleaned["home_away"].isna()
    cleaned["won"] = cleaned["result"].str.startswith("W")

    columns_to_keep = [
        "game_number",
        "date",
        "team",
        "opponent",
        "is_home",
        "runs_scored",
        "runs_allowed",
        "won"
    ]

    cleaned = cleaned[columns_to_keep]

    cleaned.to_csv(output_path, index=False)

    print(f"Cleaned data saved to {output_path}")
    print(cleaned.head())


if __name__ == "__main__":
    clean_team_schedule("DET", 2024)