import os
import time
from flask import Flask, jsonify

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def index():
    return jsonify({
        "status": "healthy",
        "message": "Welcome to DevOps Lab 2 API!",
        "environment": os.getenv("APP_ENV", "development")
    })

@app.route('/healthz')
def healthz():
    # Simulate a 10-second startup delay (e.g., waiting for database connections)
    uptime = time.time() - START_TIME
    if uptime < 10:
        return jsonify({"status": "starting", "uptime": uptime}), 500
    return jsonify({"status": "ready", "uptime": uptime}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)