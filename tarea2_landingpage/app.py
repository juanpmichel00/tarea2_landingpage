from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mysqlx import Auth
from utils.db import db
from routes.auth import auth

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(auth)
