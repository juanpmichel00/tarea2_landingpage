from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


class MessageRegistration(FlaskForm):
    name = StringField(
        validators=[InputRequired(), Length(min=1, max=30)],
        render_kw={"placeholder": "Name..."},
    )

    lastname = StringField(
        validators=[InputRequired(), Length(min=1, max=30)],
        render_kw={"placeholder": "Lastname..."},
    )

    email = StringField(
        validators=[InputRequired(), Length(min=6, max=30)],
        render_kw={"placeholder": "Email..."},
    )

    message = StringField(
        validators=[InputRequired(), Length(min=1, max=200)],
        render_kw={"placeholder": "Message..."},
    )

    submit = SubmitField("Send")
