from logicplus import app
from flask import url_for, render_template, redirect, request
from ..model.user import user
from ..model.master import master


# ------------------table user--------------
@app.route('/user', methods=['GET', 'POST'])
def tbluser():
    if request.method == 'POST':
        uid = request.form['id']
        t = {'title': 'LogicPlus | User | Update'}
        udata = user().getuserdataById(uid)
        return render_template('master/pages/tables/userform.html', row=udata, **t)

    t = {'title': 'LogicPlus | User'}
    udata = user().getuserdata()
    return render_template('master/pages/tables/tbluser.html', row=udata, username=master.__username__, **t)


@app.route('/user/update', methods=['POST'])
def update():
    if request.method == 'POST':
        uid = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mobile = request.form['mobile']
        active = request.form['active']
        valid = user().updateuserdata(uid, username, password, email, mobile, active)
        if valid is True:
            return redirect(url_for('tbluser'))


@app.route('/user/active', methods=['POST'])
def active():
    if request.method == 'POST':
        uid = request.form['id']
        if user().activateuser(int(uid)):
            return redirect(url_for('tbluser'))


@app.route('/user/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        uid = request.form['id']
        if user().inactivateuser(int(uid)):
            return redirect(url_for('tbluser'))

