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
        old_pwd = request.form['old_pwd']
        new_pwd = request.form['new_pwd']
        cnew_pwd = request.form['cnew_pwd']

        if new_pwd == cnew_pwd:
            valid = user().changepwd(master.__id__, old_pwd, new_pwd)
        if valid is True:
            return redirect(url_for('rtprofile'))
    t = {'title': 'Master | Profile'}
    return render_template('master/profile.html', username=master.__username__, **t)


# -------------------Batch-------------------------
@app.route('/batch', methods=['GET', 'POST'])
def rtbatch():
    if request.method == 'POST':
        clist = request.form.get('course_txt')
        flist = request.form.get('faculty_txt')
        print(clist, flist)
        dlist = request.form.getlist('day_txt')
        tlist = request.form.getlist('time_txt')

        if batch().addBatch(clist, flist, dlist, tlist):
            return redirect(url_for('rtblist'))
    t = {'username': master.__username__, 'title': 'Master | Batch'}
    clist = course().getCourseList()
    flist = faculty().getFacultyName()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    time = ['10:00', '12:00', '15:00']
    return render_template('master/batch/batch.html', course_list=clist, days=days, time=time,faculty_list=flist, **t)


@app.route('/batch/list', methods=['GET', 'POST'])
def rtblist():
    if request.method == 'POST':
        bid = request.form['id']
        t = {'username': master.__username__, 'title': 'Master | Batch'}
        clist = course().getCourseList()
        flist = faculty().getFacultyName()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        time = ['10:00', '12:00', '15:00']
        return render_template('master/batch/bform.html', course_list=clist, days=days, time=time, faculty_list=flist, bid=bid, **t)
    t = {'username': master.__username__, 'title': 'Master | Batch'}
    row = batch().getbatch()
    return render_template('master/batch/list.html', batch=row, **t)


@app.route('/batch/update', methods=['GET', 'POST'])
def bupdate():
    if request.method == 'POST':
        clist = request.form.get('course_txt')
        flist = request.form.get('faculty_txt')
        dlist = request.form.getlist('day_txt')
        tlist = request.form.getlist('time_txt')
        bid = request.form['id']

        if batch().updateBatch(clist, flist, dlist, tlist, bid):
            return redirect(url_for('rtblist'))


@app.route('/batch/active', methods=['GET', 'POST'])
def bactive():
    if request.method == 'POST':
        bid = request.form['id']
        if batch().Active(bid):
            return redirect(url_for('rtblist'))


@app.route('/batch/delete', methods=['GET', 'POST'])
def bdelete():
    if request.method == 'POST':
        bid = request.form['id']
        if batch().Delete(bid):
            return redirect(url_for('rtblist'))


@app.route('/invoice/list', methods=['GET', 'POST'])
def rtlist():
    if request.method == 'POST':
        t = {'username': master.__username__, 'title': 'Master | Invoice'}
        clist = course().getCourseList()
        flist = faculty().getFacultyName()
        course_name = request.form['course_txt']
        faculty_name = request.form['faculty_txt']
        invoice_data = admission().getInvoiceData(course_name,faculty_name)
        return render_template('master/invoice/list.html', course_name=clist, faculty_name=flist, row=invoice_data, **t)
    elif request.method == 'GET':
        t = {'username': master.__username__, 'title': 'Master | Invoice'}
        clist = course().getCourseList()
        flist = faculty().getFacultyName()
        invoice_data = admission().getInvoiceData()
        print(invoice_data)
        return render_template('master/invoice/list.html',course_name=clist,faculty_name=flist,row=invoice_data, **t)


@app.route('/invoice/generate/<int:aid>')
def rtinvoice(aid):
    invoice_data = admission().getInvoiceGeneratedata(aid)
    t = {'username': master.__username__, 'title': 'Master | Invoice'}
    server_time = time.strftime('%d %B %Y %A ,%H:%M:%S')
    return render_template('master/invoice/invoice.html', invoice_data=invoice_data, time=server_time, **t)


@app.route('/invoice/',methods=['GET','POST'])
def rtgenerate():
    if request.method == "POST":
        aid = request.form['name_txt']
        fees = request.form['fees_txt']
        payment_type = request.form.get('payment_type')
        valid = 0
        if payment_type == 'False':
            print("step1")
            valid = invoice().addInvoice(aid, fees)
        elif payment_type == 'True':
            bank = request.form['bank_txt']
            chq_no = request.form['chq_no']
            valid = invoice().addInvoice(aid, fees, payment_type, bank, chq_no)

        if valid is True:
            return redirect(url_for('rtinvoice', aid=aid))
    t = {'username': master.__username__, 'title': 'Invoice | Generate'}
    cname = batch().getCid()
    return render_template('master/invoice/generate.html', course_name=cname,**t)


@app.route('/invoice/get', methods=['GET', 'POST'])
def rtiData():
    cid = request.args.get('course')
    fees = course().getFeesById(cid)
    student_name = admission().getstudentNameByCid(cid)
    return jsonify(course=cid, fees=fees, sname=student_name)


@app.route('/invoice/getimage', methods=['GET'])
def getimage():
    id = request.args.get('student_name')
    paid_fees = invoice().getFeeSumByAid(id)
    dp = admission().getstudentImageById(id)

    if paid_fees[0][0] is None:
        paid_fees = 0
    else:
        paid_fees = paid_fees[0][0]
    due_fees = int(dp[0][1]) - paid_fees
    print("due_fees==", due_fees)
    return jsonify(dp=dp[0][0], due_fees=due_fees)


@app.route('/invoice/list/process', methods=['POST'])
def rtlist_process():
    if request.method == "POST":
        course_name = request.form['course_txt']
        faculty_name = request.form['faculty_txt']
        return json.dumps({'course_name': course_name, 'faculty_name': faculty_name});
