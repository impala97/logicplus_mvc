from logicplus import app
from flask import render_template, url_for, redirect, request, jsonify
from ..model.batch import batch, batch_faculty
from ..model.master import master
from ..model.course import course
from ..model.faculty import faculty


# -------------------Batch-------------------------
@app.route('/batch', methods=['GET', 'POST'])
def rtbatch():
    if request.method == 'POST':
        clist = request.form.get('course_txt')
        flist = int(request.form.get('faculty_txt'))
        dlist = request.form.getlist('day_txt')
        tlist = request.form.getlist('time_txt')
        if batch_faculty().getdt(flist, dlist, tlist) is False:
            bid = batch().addBatch(clist, flist, dlist, tlist)
            if isinstance(bid, int):
                if batch_faculty().add(flist, int(bid[0][0]), tlist):
                    return redirect(url_for('rtblist'))
    t = {'username': master.__username__, 'title': 'Master | Batch'}
    clist = course().getCourseList()
    flist = faculty().getFacultyName()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    time = ['10:00', '12:00', '15:00']
    return render_template('master/batch/batch.html', course_list=clist, days=days, time=time, faculty_list=flist, **t)


@app.route('/batch/update', methods=['GET', 'POST'])
def bupdate():
    if request.method == 'POST':
        clist = request.form.get('course_txt')
        flist = request.form.get('faculty_txt')
        dlist = request.form.getlist('day_txt')
        tlist = request.form.getlist('time_txt')
        bid = request.form['bid']
        if batch_faculty().getdt(int(flist), dlist, tlist, bid) is False:
            if batch().updateBatch(clist, flist, dlist, tlist, bid):
                if batch_faculty().add(int(flist), int(bid), tlist):
                    return jsonify(url=url_for('rtblist'), error='False')
        else:
            return jsonify(error='True', errstr="Faculty Batch time is clash with another Batch.")


@app.route('/batch/list', methods=['GET', 'POST'])
def rtblist():
    if request.method == 'POST':
        try:
            print("update")
            # bid = request.form.get("bid")
            bid = request.form['bid']
        except ValueError:
            print("error is:")
            return jsonify(status=404, data='data does not received.')
        t = {'username': master.__username__, 'title': 'Master | Batch'}
        clist = course().getCourseList()
        flist = faculty().getFacultyName()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        time = ['10:00', '12:00', '15:00']
        return render_template('master/batch/bform.html', course_list=clist, days=days, time=time, faculty_list=flist, bid=bid, **t)
    t = {'username': master.__username__, 'title': 'Master | Batch'}
    row = batch().getbatch()
    return render_template('master/batch/list.html', batch=row, **t)


@app.route('/batch/active', methods=['GET', 'POST'])
def bactive():
    if request.method == 'POST':
        print("bactive ==", request.method)
        try:
            # bid = int(request.form.get("bid"))
            bid = request.form['bid']
            print(request.form)
            print("bid", bid)
        except ValueError:
            print("error is:")
            return jsonify(status=404, data='data does not received.')
        if batch().Active(bid):
            return jsonify(url=url_for('rtblist'))


@app.route('/batch/delete', methods=['GET', 'POST'])
def bdelete():
    if request.method == 'POST':
        print("delete")
        try:
            # bid = int(request.form.get("bid"))
            bid = request.form['bid']
        except ValueError:
            return jsonify(status=404, data='data does not received.')
        if batch().Delete(bid):
            return jsonify(url=url_for('rtblist'))