import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    subprocess.call(["sudo", "systemctl", "start", "wg-quick@wg0.service"])
    return render_template("index.html")

@app.route("/stop")
def stop():
    subprocess.call(["sudo", "systemctl", "stop", "wg-quick@wg0.service"])
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
