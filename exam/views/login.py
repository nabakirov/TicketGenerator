from exam import app
from flask import request, Response, redirect, url_for, render_template, g, jsonify, abort
from exam.security import to_hash, password_verification, generate_auth_token
from ..database import Users
from ..configs import DB_PATH
from exam.security import secured

usersDB = Users(db_path=DB_PATH)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')

    email = request.form['email']
    exist = usersDB.getByEmail(email)
    if exist['code'] != 200:
        return '{}'.format(exist['message'])
    if password_verification(request.form['password'], exist['data']['password']):
        user = exist['data']

        return generate_auth_token(user)
    return 'Bad login'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('login/register.html')

    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return 'parameter is missing'
    exist = usersDB.getByEmail(email)
    if exist['code'] == 200:
        return 'user already exist by this email {}'.format(email)

    if exist['code'] != 404:
        return exist['message']
    data = {
        "email": email,
        "password": to_hash(password),
        "type": 'GOD'
    }
    response = usersDB.save(data)
    if response['code'] != 200:
        return response['message']
    token = generate_auth_token(response['data'], expiration=None)
    return token


@app.route('/update_token')
@secured('user')
def get_token():
    token = generate_auth_token(g.user)
    return token


@app.route('/protected', methods=['GET'])
@secured('user')
def protected():
    return 'Logged in as: {}\ndatabase id: {}'.format(g.user.get('email'), g.user.get('id'))
