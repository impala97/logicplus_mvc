import os
import psycopg2
from logicplus import app
from flask import redirect, request, render_template, url_for, jsonify, json
from ..model.admission import *
from ..model.batch import batch
from ..model.course import course
from ..model.faculty import faculty
from ..model.tmp import tmp
from ..model.master import master


# ----------------------Admission-----------
@app.route('/admission/add', methods=['GET', 'POST'])
def rtadmission():
    if request.method == 'POST':
        cid = request.form.get('course_txt')
        data = {}
        data.update(name=request.form['name_txt'])
        data.update(phone=request.form['phone_txt'])
        data.update(email=request.form['email_txt'])
        data.update(join=request.form['join_txt'])
        data.update(fees=request.form['fees_txt'])
        data.update(study=request.form['study_txt'])
        data.update(gender=request.form['gender'])
        data.update(details=request.form['details_txt'])
        data.update(address=request.form['address_txt'])
        data.update(cname=course().getCourseName(int(cid)))
        data.update(bid=request.form.get('batch_txt').split('_'))
        time = data['bid'][1].split(' ')
        del data['bid'][1]
        del time[0]
        print(time)
        print("len==data==", len(data))

        query = list()
        aid = admission().addAdmission(**data)
        print("len==query==", len(query))
        if not request.form.get('dp_img', None) and 'dp_img' in request.files:
            dp = request.files['dp_img']
            ufolder = 'logicplus/static/master/profile/admission'
            filename = tmp().saveIMG(dp, aid, ufolder)
            query.append(admission().updatedpById(filename, aid, string=True))
        query.append(admission_batch().add(int(aid), int(data['bid'][0]), str(time[0]), int(data['fees']), string=True))
        query.append(batch().updatecount(int(data['bid'][0]), string=True))
        try:
            if admission().call_do_bulk(query):
                return jsonify(url=url_for('rtalist'), error='False')
        except psycopg2.Error:
            admission().delete_admission(aid)
            return jsonify(error='True', errstr='Please try sometime later.')

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
    row = admission().getAdmission()
    course_data = course().getcnamebyaid()
    return render_template('master/admission/list.html', row=row, course=course_data, **t)


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
        conflict, err_str = admission_batch().getdt(aid=int(aid), bdata=bdata)
        print(err_str)
        print("conflict==", conflict)

        valid = True
        query = list()
        query.append(admission().updateAddmission(name, phone, email, study, cname[0], address, gender, join, details, int(bid[0]), aid, string=True))
        if valid is True:
            print(request.files)
            # if 'file' in request.files:
            if not request.form.get('dp_img', None) and 'dp_img' in request.files:
                ufolder = '/logicplus/static/master/profile/admission'
                old_img = admission().getimgbyid(int(aid))
                print(old_img)
                path = os.path.sep.join(app.instance_path.split(os.path.sep)[:-1]) + ufolder
                dp = request.files['dp_img']
                filename = tmp().saveIMG(dp, aid, path)
                print(filename)
                # to update image by id
                query.append(admission().updatedpById(filename, int(aid), string=True))
                query.append(admission_batch().add(int(aid), int(bid[0]), str(time[1]), int(fees), string=True))
                query.append(batch().updatecount(int(bid[0]), string=True))
                query.append(admission().updatecourse(int(aid), string=True))
                print("len==query==", len(query))
                valid = admission().call_do_bulk(query)
                print("valid==", valid)
                if valid is True:
                    tmp().remove_img(path, old_img)
                    print("old image removed.")
                    return jsonify(url=url_for('rtalist'), error='False')
                else:
                    return jsonify(error='True', err_str=err_str)
            else:
                print("image not uploaded")
                query.append(admission_batch().add(int(aid), int(bid[0]), str(time[1]), int(fees), string=True))
                query.append(admission().updatecourse(int(aid),string=True))
                query.append(batch().updatecount(int(bid[0]), string=True))
                if admission().call_do_bulk(query):
                    return jsonify(url=url_for('rtalist'), error='False')
                else:
                    return jsonify(error='True', err_str=err_str)


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
        print("aid====", aid)
        return render_template('master/admission/addcourse.html', aid=aid, c=cname, **t)


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
        flag, err_str = admission_batch().getdt(int(aid), batch_data)
        print("err_str==", err_str)
        if flag is False:
            batch_data = batch_data.split('_')
            time = batch_data[1].split(' ')
            print(admission_batch().add(int(aid), int(batch_data[0]), str(time[1]), int(fees)))
            # admission().updatecourse(**{'aid': aid, 'fees': fees, 'cname': cname[1]})
            admission().updatecourse(int(aid))
            del batch_data, aid, fees, cname
            return json.dumps({'url': url_for('rtalist'), 'error': 'False'})
        else:
            return json.dumps({'error': 'True', 'err_str': err_str})


@app.route('/admission/course/delete', methods=['POST'])
def deletecourse():
    if request.method == 'POST':
        aid = request.form["aid"]
        print(aid)
        aid = aid.split("_")
        admission().deletecourse(int(aid[0]), int(aid[1]))
        return jsonify(url=url_for('rtalist'))
