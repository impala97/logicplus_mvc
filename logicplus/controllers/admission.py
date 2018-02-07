from logicplus import app
from flask import redirect, request, render_template, url_for, flash, json
from ..model.admission import admission, admission_batch
from ..model.batch import batch
from ..model.course import course
from ..model.faculty import faculty
from ..model.tmp import tmp
from ..model.master import master


# ----------------------Admission-----------
@app.route('/admission/add', methods=['GET', 'POST'])
def rtadmission():
    if request.method == 'POST':
        dp = request.files['dp_img']
        name = request.form['name_txt']
        phone = request.form['phone_txt']
        email = request.form['email_txt']
        join = request.form['join_txt']
        fees = request.form['fees_txt']
        study = request.form['study_txt']
        gender = request.form['gender']
        details = request.form['details_txt']
        address = request.form['address_txt']
        bid = request.form.get('batch_txt').split('_')
        cid = request.form.get('course_txt')
        time = bid.split(' ')
        print(bid[0], cid)
        cname = course().getCourseName(cid)
        aid = admission().addAdmission(name, phone, email, study, cname[0], address, gender, join, fees, details, int(bid[0]))
        if aid == int(aid):
            print("aid====", aid)
            ufolder = 'logicplus/static/master/profile/admission'
            filename = tmp().saveIMG(dp, aid, ufolder)
            valid = admission().updatedpById(filename, aid)
            if valid is True:
                admission_batch().add(int(aid), int(bid[0]), str(time[1]))
                batch().updatecount(int(bid[0]))
                return redirect(url_for('rtalist'))
    t = {'username': master.__username__, 'title': 'Master | Admission'}
    cname = batch().getCid()
    return render_template('master/admission/admission.html', c=cname, **t)


@app.route('/admission/list', methods=['GET', 'POST'])
def rtalist():
    if request.method == 'POST':
        id = request.form['id']
        row = admission().getAdmission(int(id))
        t = {'username': master.__username__, 'title': 'Master | Admission'}
        cname = batch().getCid()
        return render_template('master/admission/aform.html', row=row, c=cname, **t)
    t = {'username': master.__username__, 'title': 'Master | Admission'}
    return render_template('master/admission/list.html', row=admission().getAdmission(), **t)


@app.route('/admission/update', methods=['POST'])
def rtaUpdate():
    if request.method == 'POST':
        name = request.form['name_txt']
        phone = request.form['phone_txt']
        email = request.form['email_txt']
        join = request.form['join_txt']
        fees = request.form['fees_txt']
        study = request.form['study_txt']
        gender = request.form['gender']
        details = request.form['details_txt']
        address = request.form['address_txt']
        bdata = request.form.get('batch_txt')
        bid = bdata.split('_')
        time = bid[1].split(' ')

        cid = request.form.get('course_txt')
        cname = course().getCourseName(cid)
        aid = request.form['id']
        valid = admission_batch().getdt(aid=int(aid), bdata=bdata)
        print("conflict==", valid)

        if valid is False:
            valid = admission().updateAddmission(name, phone, email, study, cname[0], address, gender, join, fees, details, int(bid[0]), aid)
            if not request.form.get('dp_img', None) and valid is not False:
                dp = request.files['dp_img']
                ufolder = 'logicplus/static/master/profile/admission'
                filename = tmp().saveIMG(dp, aid, ufolder)
                if admission().updatedpById(filename, int(aid)):
                    admission_batch().add(int(aid), int(bid[0]), str(time[1]))
                    batch().updatecount(int(bid[0]))
                    return redirect(url_for('rtalist'))
            else:
                return redirect(url_for('rtalist'))
        else:
            return json.dumps({'error': 'True', 'string': 'You have time clash with another batch.'})


@app.route('/admission/active', methods=['GET', 'POST'])
def rtaActive():
    if request.method == 'POST':
        id = request.form['id']
        valid = admission().active(int(id))
        if valid is True:
            return redirect(url_for('rtalist'))


@app.route('/admission/delete', methods=['GET', 'POST'])
def rtaDelete():
    if request.method == 'POST':
        id = request.form['id']
        valid = admission().delete(int(id))
        if valid is True:
            return redirect(url_for('rtalist'))


@app.route('/admission/batch', methods=['POST'])
def rtaData():
    if request.method == 'POST':
        cid = request.form['course_txt']
        fees = course().getFeesById(cid)
        bid, bdata = batch().getbatch(cid)
        return json.dumps({'course': cid, 'fees': fees, 'bid': bid, 'bdata': bdata})


@app.route('/admission/faculty', methods=['GET', 'POST'])
def rtaFaculty():
    batch_id = request.form['batch_txt'].split('_')
    fid = batch().getFid(int(batch_id[0]))
    faculty_name = faculty().getFacultyName(fid)
    del batch_id, fid
    return json.dumps({'fname': faculty_name})


# redirect to add course page
@app.route('/admissoin/course/', methods=['GET', 'POST'])
def rtacourse():
    if request.method == 'POST':
        t = {'username': master.__username__, 'title': 'Master | Admission'}
        cname = batch().getCid()
        aid = request.form['id']
        print(aid)
        return render_template('/master/admission/addcourse.html', aid=aid, c=cname, **t)


# for ajax data loading
@app.route('/admission/course/data', methods=['GET', 'POST'])
def rtaddcourse():
    if request.method == 'POST':
        cid = request.form['course_txt'].split(':')
        fees = course().getFeesById(cid[0])
        bid, bdata = batch().getbatch(cid[0])
        return json.dumps({'course': cid, 'fees': fees, 'bid': bid, 'bdata': bdata})


# for udpate the course details
@app.route('/admission/course/update', methods=['GET', 'POST'])
def rtupdatecourse():
    if request.method == 'POST':
        aid = request.form['aid']
        batch_data = request.form['batch_txt']
        fees = request.form['fees_txt']
        cname = request.form['course_txt'].split(':')
        if admission_batch().getdt(int(aid), batch_data) is False:
            batch_data = batch_data.split('_')
            time = batch_data[1].split(' ')
            print(admission_batch().add(int(aid), int(batch_data[0]), str(time[1])))
            # admission().updatecourse(**{'aid': aid, 'fees': fees, 'cname': cname[1]})
            admission().updatecourse(int(aid))
            del batch_data, aid, fees, cname
            return json.dumps({'url': url_for('rtalist'), 'error': 'False'})
        else:
            return json.dumps({'error': 'True', 'str': 'Your batch time is clash with another batch.'})