from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Azure web app is working!"

