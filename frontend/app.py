from flask import Flask, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load backend API base from environment
BACKEND_API = os.getenv("BACKEND_API_BASE", "http://localhost:8000/api/v1")

@app.route("/")
def index():
    """Health-check view: Fetch health status from backend API."""
    try:
        response = requests.get(f"{BACKEND_API}/health", timeout=5)
        data = response.json()
    except Exception as e:
        data = {"status": "error", "detail": str(e)}

    return render_template("index.html", data=data)

@app.route("/health")
def local_health():
    """Flask app local health check."""
    return jsonify({"frontend_status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)