def predict_game(home_team, away_team):
    home_win_probability = 0.55
    away_win_probability = 0.45

    predicted_winner = home_team if home_win_probability > away_win_probability else away_team

    return {
        "home_team": home_team,
        "away_team": away_team,
        "home_win_probability": home_win_probability,
        "away_win_probability": away_win_probability,
        "predicted_winner": predicted_winner
    }