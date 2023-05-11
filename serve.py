from flask import Flask, redirect, url_for, request
import json
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def store():
    p = subprocess.Popen(["python3", "stress_cpu.py"], shell=True)
    return "success"

@app.route('/', methods = ['GET'])
def fetch():
    ip = socket.gethostname()
    return ip


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug = True)
    app.run(debug = True)
    print(app.url_map)
