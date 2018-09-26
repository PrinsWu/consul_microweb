from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World! I am MicroUser!"

@app.route("/users", methods=["GET", "POST"])
def getUsers():
    data = buildData()
    return jsonify(data)

def buildData():
    data = {
        "users" : [
            {
                "id": "a001",
                "name": "Peter"
            },
            {
                "id": "a002",
                "name": "Mary"
            },
            {
                "id": "a003",
                "name": "Tim"
            }
        ]
    }
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)