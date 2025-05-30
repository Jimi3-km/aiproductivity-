from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to AIProductivity Pro"

if __name__ == "__main__":
    app.run(debug=True)
