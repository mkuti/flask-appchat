import os
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username.capitalize(), message))


def get_all_messages():
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)


@app.route("/")
def index():
    """ Main page with instructions """
    return render_template("index.html")


@app.route("/<username>")
def user(username):
    return "<h1>Welcome {0} </h1>{1}".format(username.capitalize(), get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=True)