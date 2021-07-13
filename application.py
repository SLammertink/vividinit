from forms import ContactForm
from flask import Flask, render_template, request, flash
from flask_mail import Message, Mail
import os
import sqlite3
from dotenv import load_dotenv
load_dotenv()


application = Flask(__name__)

application.config['SECRET_KEY'] = os.getenv('SecretKey')

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv('EMAIL_USER'),
    "MAIL_PASSWORD": os.getenv('EMAIL_PASSWORD'),
    "MAIL_DEFAULT_SENDER": os.getenv('DEFAULT_EMAIL')
}
application.config.update(mail_settings)
mail = Mail(application)
application.config.update(mail_settings)


# start of the application
@application.route('/index')
@application.route('/')
@application.route('/home')
def index():
    return render_template('index.html')


@application.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            flash("Message successfully send!")
            msg = Message(form.subject.data, recipients=[
                os.getenv('DEFAULT_EMAIL')])
            msg.body = """
            From: %s
            Email: %s
            Message: %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            conn = sqlite3.connect('clientlog.db')
            curs = conn.cursor()
            # Create table
            curs.execute('''CREATE TABLE IF NOT EXISTS clientlog
            (timestamp DATETIME, name TEXT, email TEXT, message TEXT)''')
            curs.execute("INSERT INTO clientlog values(datetime('now'), (?), (?), (?))", [
                         form.name.data, form.email.data, form.message.data])
            conn.commit()
            conn.close()
            return render_template('index.html', form=form)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')


if __name__ == '__main__':
    application.run(debug=True)
