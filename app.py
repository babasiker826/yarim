from flask import Flask, send_from_directory, render_template, jsonify
import os

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/files/<filename>")
def serve_file(filename):
    allowed_files = ["Sevgilim.mp3", "yağmur.mp3"]
    if filename in allowed_files:
        return send_from_directory(".", filename)
    return "Dosya bulunamadı", 404

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"}), 200
