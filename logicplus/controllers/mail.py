from logicplus import app
from flask_mail import Mail, Message
from flask import flash, request, redirect, url_for
import time

app.config['SECRET_KEY'] = 'logicplus'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'vcr.student@gmail.com'
app.config['MAIL_PASSWORD'] = 'eclassroom'
mail = Mail(app)


def sent(recipients, subject, body):
    msg = Message(subject=subject, sender=("VCR", "vcr.faculty@gmail.com"), recipients=[recipients])
    assert msg.sender == "VCR <vcr.faculty@gmail.com>"
    msg.body = "Task List %s %s" % (body, msg.sender)
    msg.html = "<html><body><table style='border:3px;'><tr><td>Hello</td><td>1:45</td></tr></table></body></html>"
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

