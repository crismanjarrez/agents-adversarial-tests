"""
Sample Flask application - baseline for security testing.
"""
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///app.db")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/data")
def get_data():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id required"}), 400
    return jsonify({"user_id": user_id, "data": []})


if __name__ == "__main__":
    app.run(debug=False)
