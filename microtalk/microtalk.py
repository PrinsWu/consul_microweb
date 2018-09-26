from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World! I am MicroTalk!"

@app.route("/talks", methods=["GET", "POST"])
def getTalks():
    data = buildData()
    return jsonify(data)

def buildData():
    data = {
        "talks" : [
            {
                "id": "t001",
                "talker_id": "a001",
                "talker_name": "Peter",
                "msg": "Hello World!",
                "datetime": "2018/09/17 13:00"
            },
            {
                "id": "t002",
                "talker_id": "a002",
                "talker_name": "Mary",
                "msg": "Hi!",
                "datetime": "2018/09/17 13:01"
            },
            {
                "id": "t002",
                "talker_id": "a003",
                "talker_name": "Tim",
                "msg": "Hello!",
                "datetime": "2018/09/17 13:02"
            },
            {
                "id": "t003",
                "talker_id": "a001",
                "talker_name": "Peter",
                "msg": "Fine thank you!",
                "datetime": "2018/09/17 13:03"
            }
        ]
    }
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)