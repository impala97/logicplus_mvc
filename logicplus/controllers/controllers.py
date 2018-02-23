from logicplus import app
import time
from flask import redirect, url_for, render_template, request, flash, session, jsonify, json
from ..model.user import user
from ..model.master import master
from ..model.faculty import faculty
from ..model.course import course
from ..model.admission import admission,admission_batch
from ..model.batch import batch
from ..model.invoice import invoice
from ..model.chat import chat


@app.route('/', methods=['GET', 'POST'])
def rtlogin():
    if request.method == 'POST':
        row = user().do_login(username=request.form['un_txt'])
        if request.form['un_txt'] is None or request.form['pwd_txt'] is None:
            flash(message='Invalid Username or Password.')
            return redirect(url_for('rtlogin'))
        elif row[0][1] == request.form['un_txt']:
            if row[0][2] == request.form['pwd_txt']:
                if user().update_login(row[0][0]) is True and row[0][6] is False:
                    master.__username__ = request.form['un_txt']
                    master.__id__ = user().__getId__(master.__username__)
                    master.__email__ = user().__getEmail__(master.__id__)
                    print(master.__username__, master.__id__, master.__email__)
                    if user().update_login(master.__id__) is True:
                        session['logged_in'] = master.__username__
                        return redirect(url_for('rtindex'))
            else:
                flash(message='Password Does not match.')
                return redirect(url_for('rtlogin'))
        else:
            flash(message='Invalid username')
            return redirect(url_for('rtlogin'))
    data = {'tilte': 'LogicPlus | Login'}
    return render_template('master/login.html', **data)


@app.route('/register', methods=['GET', 'POST'])
def rtregister():
    if request.method == 'POST':
        un = request.form['un_txt']
        email = request.form['email_txt']
        mobile = request.form['mobile_txt']
        pwd = request.form['pwd_txt']
        cpwd = request.form['cpwd_txt']

        if un is not None and email is not None and mobile is not None and pwd is not None and cpwd is not None:
            if pwd != cpwd:
                flash(message='password not match.')
                return redirect(url_for('rtregister'))
            elif pwd == cpwd:
                valid = user().adduser(un, pwd, email, mobile)

                if valid is not False:
                    session['username'] = un
                    master.__id__ = valid
                    master.__username__ = un
                    master.__email__ = email
                    print(master.__id__, master.__email__, master.__username__)
                    return redirect(url_for('rtindex'))
                else:
                    return "User already exists!"
        else:
            flash(message='Please enter valid data.')
            return redirect(url_for('rtregister'))

    data = {'title': 'LogicPlus | Registeration'}
    return render_template('master/register.html', **data)


@app.route('/index', methods=['GET'])
def rtindex():
    if request.method == 'POST':
        return "index==post"
    t = {'title': 'LogicPlus | Index'}
    chat_data = chat().getchat()
    count = dict()
    count["user"] = user().usercount()
    count["fees"] = invoice().getFeeSumByAid()
    count["student"] = admission().coountid()
    count["faculty"] = faculty().countid()
    return render_template('master/index.html', username=master.__username__,chat_data=chat_data, **t,**count)


@app.route('/simple')
def simple():
    data = {'title': 'LogicPlus | Simple'}
    return render_template('master/pages/tables/simple.html', username=master.__username__, **data)


@app.route('/data')
def data():
    data = {'title': 'LogicPlus | Data'}
    return render_template('master/pages/tables/data.html', username=master.__username__, **data)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if user().update_logout(session.get('logged_in')) is True:
        session['logged_in'] = 0
        flash(message='You were logger out')
        del master.__id__, master.__username__
        return redirect(url_for('rtlogin'))


@app.route('/profile', methods=['GET', 'POST'])
def rtprofile():
    if request.method == 'POST':
        print(request.method)
        print(request.form)
        old_pwd = request.form['old_pwd']
        new_pwd = request.form['new_pwd']
        cnew_pwd = request.form['cnew_pwd']

        if new_pwd == cnew_pwd:
            valid = user().changepwd(int(master.__id__), old_pwd, new_pwd)
            if valid is True:
                return jsonify(url=url_for('rtindex'), status=200)
    t = {'title': 'Master | Profile'}
    return render_template('master/profile.html', username=master.__username__, **t)
