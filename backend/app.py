from flask import Flask, jsonify, request
from predictor import predict_game

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

    prediction = predict_game(home_team, away_team)

    return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)