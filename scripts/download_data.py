import pandas as pd


TEAMS = ["DET", "NYY", "BOS", "LAD", "CHC"]


def download_team_schedule(team, year):
    url = f"https://www.baseball-reference.com/teams/{team}/{year}-schedule-scores.shtml"
    print(f"Downloading {team} {year} data...")

    tables = pd.read_html(url)
    games = tables[0]

    games = games[games["Gm#"] != "Gm#"]

    output_path = f"data/raw/{team}_{year}_games.csv"
    games.to_csv(output_path, index=False)

    print(f"Saved {len(games)} games to {output_path}")


def download_multiple_teams(year):
    for team in TEAMS:
        download_team_schedule(team, year)


if __name__ == "__main__":
    download_multiple_teams(2024)