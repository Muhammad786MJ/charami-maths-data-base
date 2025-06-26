# app.py
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open("videos.json", encoding="utf-8") as f:
        videos = json.load(f)
    return render_template("index.html", videos=videos)

@app.route('/api/videos')
def api_videos():
    with open("videos.json", encoding="utf-8") as f:
        videos = json.load(f)
    return jsonify(videos)

if __name__ == '__main__':
    app.run(debug=True)
