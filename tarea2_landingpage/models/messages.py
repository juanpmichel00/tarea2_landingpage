from utils.db import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    message = db.Column(db.String(50), nullable=True)

    def __init__(self, name, lastname, email, message) -> None:
        self.name = name
        self.lastname = lastname
        self.email = email
        self.message = message

    def __repr__(self) -> str:
        return f"Message({self.id}, '{self.name}', '{self.lastname}', '{self.email}', '{self.message}')"
