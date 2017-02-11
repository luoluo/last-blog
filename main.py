import flask
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test_render")
def test_render():
    return render_template("hello.html")

@app.route("/user/<name>")
def hello_you(name):
    return "Hello {}!".format(name)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
