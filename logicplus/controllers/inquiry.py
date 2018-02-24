from logicplus import app
from flask import render_template, url_for, flash, redirect, request, json
from ..model.inquiry import inquiry
from ..model.master import master
from ..model.batch import batch
from ..model.course import course


# --------------------Inquiry---------------------------
@app.route('/inquiry/add', methods=['GET', 'POST'])
def addinquiry():
    if request.method == 'POST':
        name = request.form['name_txt']
        email = request.form['email_txt']
        phone = request.form['phone_txt']
        course_list = request.form.getlist("course_txt")
        course_txt = ""
        if len(course_list) > 0:
            for i in range(len(course_list)):
                tmp = course_list[i].split(':')
                if i == 0:
                    course_txt = tmp[1]
                else:
                    course_txt = course_txt + "," + tmp[1]
        study = request.form['study_txt']
        details = request.form['details_txt']
        gender = request.form['gender']
        status = request.form['status_txt']

        if name is not None and email is not None and phone is not None and course_txt is not None and study is not None and details is not None:
            rid = inquiry().addInquiry(name, email, phone, course_txt, study, details, gender, status)
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
        course_list = request.form.getlist("course_txt")
        course_txt = ""
        if len(course_list) > 0:
            for i in range(len(course_list)):
                tmp = course_list[i].split(':')
                if i == 0:
                    course_txt = tmp[1]
                else:
                    course_txt = course_txt + "," + tmp[1]
        study = request.form['study_txt']
        details = request.form['details_txt']
        gender = request.form['gender']
        status = request.form['status_txt']
        iid = request.form['iid']
        if name is not None and email is not None and phone is not None and course_txt is not None and study is not None and details is not None:
            rid = inquiry().updateInquiry(iid, name, email, phone, course_txt, study, details, gender, status)
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
        print(inquiry_data)
        cname = batch().getCid()
        title = 'Master | Inquiry'
        return render_template('master/inquiry/updateinquiry.html', c=cname, row=inquiry_data, username=master.__username__, title=title)
    title = {'title': 'Master | Faculty'}
    udata = inquiry().getinquiry()
    print(udata)
    return render_template('master/inquiry/list.html', row=udata, username=master.__username__, **title)


@app.route('/inquiry/active', methods=['POST'])
def inquiryActive():
    if request.method == 'POST':
        inquiry_id = request.form['id']
        if inquiry().activateInquiry(int(inquiry_id)):
            return redirect(url_for('inquirylist'))
        else:
            return redirect(url_for('inquirylist'))


@app.route('/inquiry/delete', methods=['POST'])
def inquiryDelete():
    if request.method == 'POST':
        inquiry_id = request.form['id']
        if inquiry().inactivateInquiry(int(inquiry_id)):
            return redirect(url_for('rtilist'))
        else:
            return redirect(url_for('rtilist'))


@app.route('/course/data', methods=['POST'])
def coursedata():
    if request.method == 'POST':
        course_txt = request.form['course_txt']
        if course_txt != 'null':
            course_txt = json.loads(course_txt)
            fees = 0
            for i in range(len(course_txt)):
                cid = course_txt[i].split(':')
                fees += course().getFeesById(cid[0])
            del cid, course_txt
            return json.dumps({'fees': fees})
        else:
            return json.dumps({'fees': 0})


@app.route('/inquiry/notes', methods=['GET', 'POST'])
def rtnotes():
    if request.method == 'POST':
        t = {'title': 'Add Notes | Inquiry', 'username': master.__username__}
        inquiry_id = request.form["id"]
        row = inquiry().getnotes(int(inquiry_id))
        return render_template('master/inquiry/notes.html', row=row, **t)
