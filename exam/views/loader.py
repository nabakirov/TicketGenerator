from exam import app
from flask import render_template, redirect
from exam.security import secured

@app.route('/')
def index_template():
    return render_template('index.html')


@app.route('/login')
def login_template():
    return render_template('login/login.html')

@app.route('/register')
def register_template():
    return render_template('login/register.html')