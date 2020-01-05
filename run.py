import os
from flask import Flask

app = Flask(__name__)
messages = []


def add_messages(username, message):
    messages.append("{}: {}".format(username, message))


@app.route("/")
def index():
    """ Main page with instructions """
    return "To send a message use: /USERNAME/MESSAGE"


@app.route("/<username>")
def user(username):
    return "Welcome {0}".format(username)


@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)