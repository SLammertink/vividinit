from flask_wtf import CsrfProtect, Form
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import Email

csrf = CsrfProtect()


class ContactForm(Form):
    name = StringField('Name', [
        validators.DataRequired()])

    email = StringField('E-mail', [
        validators.DataRequired('E-mail address is required'),
        Email('Please enter a valid email address')])

    subject = StringField('Subject', [
        validators.DataRequired('Please enter a subject')])

    message = TextAreaField('Message', [
        validators.DataRequired('Please enter a message')])

    submit = SubmitField("Send")
