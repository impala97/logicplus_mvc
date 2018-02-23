from flask import request, url_for, render_template, redirect, json, jsonify
from logicplus import app
from ..model.admission import admission
from ..model.course import course
from ..model.faculty import faculty
from ..model.invoice import invoice
from ..model.master import master


@app.route('/invoice/list', methods=['GET', 'POST'])
def rtlist():
    if request.method == 'POST':
        t = {'username': master.__username__, 'title': 'Master | Invoice'}
        clist = course().getCourseList()
        flist = faculty().getFacultyName()
        course_name = request.form['course_txt']
        faculty_name = request.form['faculty_txt']
        print(course_name)
        invoice_data = admission().getInvoiceData(int(course_name), int(faculty_name))
        print(invoice_data)
        return render_template('master/invoice/list.html', course_name=clist, faculty_name=flist, row=invoice_data, **t)
    elif request.method == 'GET':
        t = {'username': master.__username__, 'title': 'Master | Invoice'}
        clist = course().getCourseList()
        flist = faculty().getFacultyName()
        invoice_data = admission().getInvoiceData()
        print(invoice_data)
        return render_template('master/invoice/list.html', course_name=clist, faculty_name=flist, row=invoice_data, **t)


@app.route('/invoice/generate/<int:aid>')
def rtinvoice(aid):
    invoice_data = admission().getInvoiceGeneratedata(aid)
    t = {'username': master.__username__, 'title': 'Master | Invoice'}
    server_time = time.strftime('%d %B %Y %A ,%H:%M:%S')
    return render_template('master/invoice/invoice.html', invoice_data=invoice_data, time=server_time, **t)


@app.route('/invoice/', methods=['GET', 'POST'])
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
    paid_fees = invoice().getFeeSumByAid(int(id))
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
        return json.dumps({'course_name': course_name, 'faculty_name': faculty_name})
