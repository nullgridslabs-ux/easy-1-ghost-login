# easy-1-ghost-login/app.py
from flask import Flask, request, session, jsonify
from flask_session import Session
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "ghost"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

FLAG = os.environ.get("FLAG", "CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/auth/start", methods=["POST"])
def start():
    data = request.json or {}
    if data.get("email"):
        # BUG: authenticated too early
        session["auth"] = True
    return jsonify({"msg": "OTP sent"})

@app.route("/dashboard")
def dashboard():
    if not session.get("auth"):
        return jsonify({"error": "login required"}), 401
    return jsonify({"flag": FLAG})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
