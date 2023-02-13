from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return "Get has been completed"

@app.route('/', methods=['PUT'])
def put():
    return "Put complete"

@app.route('/', methods=['DELETE'])
def delete():
    return "Delete complete"