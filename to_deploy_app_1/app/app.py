from flask import Flask
from app.config import configurations


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return {
        'color': configurations.COLOR,
        'domain': configurations.DOMAIN_NAME
    }


@app.route("/internal/liveness", methods=["GET"])
def liveness():
    return {"hello": "i am alive"}
