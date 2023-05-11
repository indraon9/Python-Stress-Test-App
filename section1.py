from flask import Flask, redirect, url_for, request
import json

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def store():
    body = request.get_json(force=True)
    with open("seed", "w") as f:
      f.writelines(body["num"])
    return "success"

@app.route('/', methods = ['GET'])
def fetch():
  seed = 0
  with open("seed") as f:
    seed = f.readline()
  return seed


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug = True)
    #app.run(debug = True)
    print(app.url_map)
