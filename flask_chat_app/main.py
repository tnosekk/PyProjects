import random
from string import ascii_uppercase

from flask import Flask, redirect, render_template, request, session
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)

app.config["SECRET_KEY"] = "key"
socketio = SocketIO(app)


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
