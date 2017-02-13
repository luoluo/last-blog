import flask
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from resources import Resources

app = Flask(__name__)
resources = Resources()
resources.load_post()

@app.route("/about")
def about():
    # return render_template("about.html")
    return redirect(url_for("construct"))

@app.route("/archives/")
def archives():
    return render_template("archives.html", posts=resources.posts())

@app.route("/archives/<string:archive_id>")
def archive(archive_id):
    return render_template("post.html", post=resources.get(archive_id))

@app.route("/construct")
def construct():
    return render_template("construct.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("construct.html")

@app.route("/dev")
def dev():
    return redirect(url_for("archives"))

@app.route("/")
def hello():
    #return redirect(url_for("construct"))
    return redirect(url_for("dev"))

if __name__ == "__main__":
    app.run()
