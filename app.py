from flask import Flask, render_template, jsonify
import threading
import webbrowser
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text')
def get_text():
    filename = "text-to-type.txt"
    if not os.path.exists(filename):
        return jsonify({"error": "File not found"}), 404

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    return jsonify({"text": content})

def run_server():
    app.run(port=5000)

if __name__ == "__main__":
    threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:5000/")).start()
    run_server()