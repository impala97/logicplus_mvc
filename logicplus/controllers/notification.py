from logicplus import app
from flask import url_for, render_template, redirect, request


@app.route('/mailnote/course/time', methods=['GET', 'POST'])
def coursetime():
    pass