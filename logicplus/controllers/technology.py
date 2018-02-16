from logicplus import app
from flask import url_for, request, redirect, render_template, flash, json
from ..model.tech import tech
from ..model.tmp import tmp
from ..model.master import master


# -----------------technology----------------
@app.route('/technology', methods=['GET', 'POST'])
def tbltech():
    if request.method == 'POST':
        id = request.form['id']
        t = {'title': 'LogicPlus | Technology'}
        udata = tech().getTech(id)
        return render_template('master/technology/techform.html', row=udata, **t)
    t = "Master | Technology"
    udata = tech().gettechnology()
    udata = tmp().sort(udata)
    data = tech().getTech()
    return render_template('master/technology/technology.html', menu=udata, row=data, title=t)


@app.route('/technology/update', methods=['POST'])
def techUpdate():
    if request.method == 'POST':
        id = request.form['id']
        technology = request.form['technology']
        framework = request.form['framework']
        valid = tech().updateTechnology(id, technology, framework)
        if valid is True:
            return redirect(url_for('tbltech'))


@app.route('/technology/active', methods=['POST'])
def techActive():
    if request.method == 'POST':
        id = request.form['id']
        if tech().activatetech(int(id)):
            return redirect(url_for('tbltech'))
        else:
            return redirect(url_for('tbltech'))


@app.route('/technology/delete', methods=['POST'])
def techDelete():
    if request.method == 'POST':
        id = request.form['id']
        if tech().inactivatetech(int(id)):
            return redirect(url_for('tbltech'))
        else:
            return redirect(url_for('tbltech'))


@app.route('/technology/add', methods=['GET', 'POST'])
def addtech():
    if request.method == 'POST':
        print("form===", request.form['Framework'])
        print(request.get_json())
        print(request.form['data.name'])
        print(request.form['data.framework'])
        print(request.form.get("name"))
        print(request.form.get("data.name"))
        print(request.json)
        name = request.form.get("tech.name")
        framework = request.form.get("tech.framework")
        # valid = tech().addtech(request.form['Technology'], request.form['Framework'])
        valid = tech().addtech(name, framework)
        if valid is True:
            message = "%s | %s" % (request.form['Technology'], request.form['Framework'])
            flash(message, 'add')
            return redirect(url_for('addtech'))
    t = {'title': 'Master | Add Technology'}
    return render_template('master/technology/add.html', username=master.__username__, **t)
