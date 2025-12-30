from flask import Flask, jsonify, render_template
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask DevOps CI/CD application is running 🚀"

@app.route("/health")
def health():
    return jsonify(
        status="UP",
        message="Application is healthy"
    )

@app.route("/info")
def info():
    return jsonify(
        app="DevOps CI/CD Project",
        version="1.0.0",
        hostname=socket.gethostname(),
        environment=os.getenv("ENV", "production")
    )

@app.route("/time")
def time():
    return jsonify(
        server_time=datetime.datetime.utcnow().isoformat() + "Z"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
