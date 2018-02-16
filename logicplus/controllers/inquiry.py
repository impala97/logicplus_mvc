from logicplus import app
from flask import render_template,url_for,flash,redirect,request
from ..model.inquiry import inquiry
from ..model.master import master
from ..model.batch import batch


# --------------------Inquiry---------------------------
@app.route('/inquiry/add', methods=['GET', 'POST'])
def addinquiry():
    if request.method == 'POST':
        name = request.form['name_txt']
        email = request.form['email_txt']
        phone = request.form['phone_txt']
        course_txt = request.form['course_txt'].split(':')
        study = request.form['study_txt']
        details = request.form['details_txt']
        gender = request.form['gender']

        if name is not None and email is not None and phone is not None and course_txt[1] is not None and study is not None and details is not None:
            rid = inquiry().addInquiry(name, email, phone, course_txt[1], study, details, gender)
            if rid is not False:
                flash('Inquiry inserted!')
                return redirect(url_for('inquirylist'))
        else:
            flash('Enter All Feilds Data')
            return redirect(url_for('addinquiry'))
    t = {'title': 'Master | Inquiry'}
    cname = batch().getCid()
    return render_template('master/inquiry/addinquiry.html', username=master.__username__, c=cname, **t)


@app.route('/inquiry/update/', methods=['POST'])
def updateinquiry():
    if request.method == 'POST':
        name = request.form['name_txt']
        email = request.form['email_txt']
        phone = request.form['phone_txt']
        course_txt = request.form['course_txt'].split(':')
        study = request.form['study_txt']
        details = request.form['details_txt']
        gender = request.form['gender']
        iid = request.form['iid']
        if name is not None and email is not None and phone is not None and course_txt[1] is not None and study is not None and details is not None:
            rid = inquiry().updateInquiry(iid, name, email, phone, course_txt[1], study, details, gender)
            if rid is not False:
                flash('Inquiry Updated!')
                return redirect(url_for('inquirylist'))
        else:
            flash('Enter All Feilds Data')
            return redirect(url_for('inquirylist'))


@app.route('/inquiry/list', methods=['GET', 'POST'])
def inquirylist():
    if request.method == 'POST':
        iid = request.form['iid']
        inquiry_data = inquiry().getdataById(iid)
        cname = batch().getCid()
        title = 'Master | Inquiry'
        return render_template('master/inquiry/updateinquiry.html', c=cname, row=inquiry_data, username=master.__username__, title=title)
    title = {'title': 'Master | Faculty'}
    udata = inquiry().getinquiry()
    return render_template('master/inquiry/list.html', row=udata, username=master.__username__, **title)


@app.route('/inquiry/active', methods=['POST'])
def inquiryActive():
    if request.method == 'POST':
        id = request.form['id']
        if inquiry().activateInquiry(int(id)):
            return redirect(url_for('inquirylist'))
        else:
            return redirect(url_for('inquirylist'))


@app.route('/inquiry/delete', methods=['POST'])
def inquiryDelete():
    if request.method == 'POST':
        id = request.form['id']
        if inquiry().inactivateInquiry(int(id)):
            return redirect(url_for('rtilist'))
        else:
            return redirect(url_for('rtilist'))