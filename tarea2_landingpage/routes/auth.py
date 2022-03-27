from typing_extensions import Self
from flask import Blueprint, render_template, redirect, url_for
from utils.db import db
from forms.messageForm import MessageRegistration
from models.messages import Message


auth = Blueprint("auth", __name__)


@auth.route("/")
def comms():
    form = MessageRegistration()
    if form.validate_on_submit():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        message = form.message.data
        newMessage = Message(name, lastname, email, message)
        db.session.add(newMessage)
        db.session.commit()
        return "Message sent"
    return render_template("landingpage.html")
