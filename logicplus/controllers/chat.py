from logicplus import app
from flask import url_for, redirect, request
from ..model.chat import chat
from ..model.master import master


@app.route('/index', methods=['POST'])
def rtchat():
    if request.method == 'POST':
        chat_data = dict()
        chat_data['name'] = str(master().user())
        chat_data['message'] = str(request.form['message_txt'])
        if chat().addchat(**chat_data):
            return redirect(url_for('rtindex'))
        else:
            return "due to some error you have been logout."


