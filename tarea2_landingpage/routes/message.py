from flask import Blueprint, render_template
from models.messages import Message


messaging = Blueprint("message", __name__, url_prefix="/")


@messaging.route("/messages", methods=["GET", "POST"])
def message():
    messageList = Message.query.all()
    return render_template("messages.html", messageList=messageList)
