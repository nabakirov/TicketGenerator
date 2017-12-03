from exam import app
from flask import request, Response, redirect, url_for, render_template
from exam.login import User, toHash, hashCompare
from ..database import Users
import flask_login
from ..configs import DB_PATH

usersDB = Users(db_path=DB_PATH)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')

    email = request.form['email']
    exist = usersDB.getByEmail(email)
    if exist['code'] != 200:
        return '{}'.format(exist['message'])
    if hashCompare(toHash(request.form['password']), exist['data']['password']):
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for(''))
    return 'Bad login'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('login/register.html')
    email = request.form['email']
    password = request.form['password']
    exist = usersDB.getByEmail(email)
    if exist['code'] == 200:
        return 'user already exist by this email {}'.format(email)

    if exist['code'] != 404:
        return exist['message']
    data = {
        "email": email,
        "password": toHash(password)
    }
    response = usersDB.save(data)
    if response['code'] != 200:
        return response['message']
    return 'account created successfully'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id
