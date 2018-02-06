from logicplus import app
from flask_mail import Mail, Message
from flask import flash, request, redirect, url_for
from ..model.master import master
import time

app.config['SECRET_KEY'] = 'logicplus'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'vcr.student@gmail.com'
app.config['MAIL_PASSWORD'] = 'eclassroom'
mail = Mail(app)


def sent(recipients, subject, body, html=None):
    msg = Message(subject=subject, sender=(master().user(), app.config['MAIL_USERNAME']), recipients=[recipients])
    msg.body = "%s %s" % (body, msg.sender)
    if html is not None:
        msg.html = str(html)
    mail.connect()
    time.strftime('%A ,%d %B %Y %H:%M:%S')
    mail.send(msg)
    return True


@app.route('/mail', methods=['GET', 'POST'])
def rtmail():
    if request.method == 'POST':
        toaddrs = request.form['email_txt']
        subject = request.form['subject_txt']
        msg = request.form['msg_txt']
        if sent(toaddrs, subject, msg):
            flash("Email Sent!")
            return redirect(url_for('rtindex'))
    return "Sent"

