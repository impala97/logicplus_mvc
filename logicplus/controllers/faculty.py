from logicplus import app
from flask import url_for, render_template, redirect, request
from ..model.faculty import faculty
from ..model.master import master
from ..model.batch import batch_faculty
from ..model.tmp import tmp


# -----------faculty--------------------
@app.route('/faculty/add', methods=['GET', 'POST'])
def addfaculty():
    if request.method == 'POST':
        name = request.form['name_txt']
        email = request.form['email_txt']
        phone = request.form['phone_txt']
        website = request.form['ws_txt']
        company = request.form['company_txt']
        post = request.form['post_txt']
        dob = request.form['dob_txt']
        address = request.form['address_txt']
        gender = request.form['gender']

        if name is not None and email is not None and phone is not None and website is not None and company is not None and post is not None and dob is not None and address is not None:
            rid = faculty().addFaculty(name, email, phone, website, company, post, dob, address, gender)
            img = request.files['dp_img']
            valid = tmp().saveIMG(img, rid)
            if valid is not False:
                flash('Image saved!!')
                return redirect(url_for('facultyprofile'))
        else:
            flash('Enter All Feilds Data')
            return redirect(url_for('facultyprofile'))
    title = 'Master | Faculty'
    return render_template('master/faculty/addfaculty.html', title=title)


@app.route('/faculty/update', methods=['POST'])
def updatefaculty():
    if request.method == 'POST':
        if request.method == 'POST':
            name = request.form['name_txt']
            email = request.form['email_txt']
            phone = request.form['phone_txt']
            website = request.form['ws_txt']
            company = request.form['company_txt']
            post = request.form['post_txt']
            dob = request.form['dob_txt']
            address = request.form['address_txt']
            gender = request.form['gender']
            id = request.form['sid']
            valid = faculty().updateFaculty(id, name, email, phone, website, company, post, dob, address, gender)
            if valid is True:
                file = request.files['dp_img']
                filename = tmp().saveIMG(file, id)
                valid = faculty().updateimg(filename, id)
                if valid is not False:
                    flash('updated successfully!!')
                    return redirect(url_for('facultyprofile'))


@app.route('/faculty/profile/', methods=['GET', 'POST'])
def facultyprofile():
    if request.method == 'POST':
        fid = request.form['fid']
        faculty_data = faculty().getdataById(fid)
        title = 'Master | Faculty'
        return render_template('master/faculty/updatefaculty.html', row=faculty_data, title=title)
    title = 'Master | Faculty'
    faculty_data = faculty().getfacultydata()
    return render_template('/master/faculty/facultyprofile.html', row=faculty_data, username=master.__username__, title=title)
    del faculty_data


@app.route('/faculty/active', methods=['POST'])
def facultyActive():
    if request.method == 'POST':
        id = request.form['id']
        if faculty().activateFaculty(int(id)):
            return redirect(url_for('facultyprofile'))
        else:
            return redirect(url_for('facultyprofile'))


@app.route('/faculty/delete', methods=['POST'])
def facultyDelete():
    if request.method == 'POST':
        id = request.form['id']
        if faculty().inactivateFaculty(int(id)):
            return redirect(url_for('facultyprofile'))
        else:
            return redirect(url_for('facultyprofile'))