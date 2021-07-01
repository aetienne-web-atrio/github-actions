from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Guy de lusignan</h1><p>Hello, World! HEY now here</p>"
