from logicplus import app
from flask import url_for, render_template, request, redirect, json
from ..model.course import course
from ..model.master import master


# ----------------------course-----------
@app.route('/course/data', methods=['POST'])
def coursedata():
    if request.method == 'POST':
        cid = request.form['course_txt'].split(':')
        fees = course().getFeesById(cid[0])
        del cid
        return json.dumps({'fees': fees})


@app.route('/course', methods=['GET', 'POST'])
def rtcourse():
    if request.method == 'POST':
        cname = request.form['cname_txt']
        duration = request.form['duration_txt']
        details = request.form['details_txt']
        fees = request.form['fees_txt']
        if course().addCourse(cname, duration, fees, details):
            return redirect(url_for('rtclist'))
    t = {'username': master.__username__, 'title': 'Master | Course'}
    return render_template('master/course/course.html', **t)


@app.route('/course/list', methods=['GET', 'POST'])
def rtclist():
    if request.method == 'POST':
        id = request.form['id']
        t = {'username': master.__username__, 'title': 'Master | Course'}
        return render_template('master/course/cform.html', row=course().getCourseData(int(id)), **t)
    t = {'username': master.__username__, 'title': 'Master | Course'}
    return render_template('master/course/list.html', row=course().getCourseData(), **t)


@app.route('/course/update', methods=['GET', 'POST'])
def cupdate():
    if request.method == 'POST':
        id = request.form['id']
        cname = request.form['cname_txt']
        duration = request.form['duration_txt']
        details = request.form['details_txt']
        fees = request.form['fees_txt']
        if course().updateCourse(cname, duration, int(fees), details, int(id)):
            return redirect(url_for('rtclist'))


@app.route('/course/active', methods=['GET', 'POST'])
def cactive():
    if request.method == 'POST':
        id = request.form['id']
        valid = course().active(int(id))
        if valid is True:
            return redirect(url_for('rtclist'))


@app.route('/course/delete', methods=['GET', 'POST'])
def cdelete():
    if request.method == 'POST':
        id = request.form['id']
        valid = course().delete(int(id))
        if valid is True:
            return redirect(url_for('rtclist'))
