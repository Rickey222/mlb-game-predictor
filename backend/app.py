from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "MLB Game Predictor API is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/predict")
def predict():
    home_team = request.args.get("home_team", "DET")
    away_team = request.args.get("away_team", "NYY")

    # Temporary placeholder prediction
    home_win_probability = 0.55
    away_win_probability = 0.45

    predicted_winner = home_team if home_win_probability > away_win_probability else away_team

    return jsonify({
        "home_team": home_team,
        "away_team": away_team,
        "home_win_probability": home_win_probability,
        "away_win_probability": away_win_probability,
        "predicted_winner": predicted_winner
    })


if __name__ == "__main__":
    app.run(debug=True)