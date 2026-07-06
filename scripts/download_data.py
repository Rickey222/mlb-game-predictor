import pandas as pd


def download_season(year, team):
    url = f"https://www.baseball-reference.com/teams/{team}/{year}-schedule-scores.shtml"
    print(f"Downloading data from {url}")

    tables = pd.read_html(url)
    games = tables[0]

    games = games[games["Gm#"] != "Gm#"]

    output_path = f"data/raw/{team}_{year}_games.csv"
    games.to_csv(output_path, index=False)

    print("\nDownload complete!")
    print(f"Number of games: {len(games)}")
    print("\nColumns:")
    print(games.columns.tolist())
    print("\nFirst 5 rows:")
    print(games.head())
    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    download_season(2024, "DET")