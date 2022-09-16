from flask import Flask, render_template
from threading import Thread
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    return "running"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()