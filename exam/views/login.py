from exam import app
from flask import request, Response, redirect, url_for, render_template, g, jsonify, abort
from exam.security import to_hash, password_verification, generate_auth_token
from ..database import Users
from ..configs import DB_PATH
from exam.security import secured
from exam.utils import getargs, HTTP_ERR, HTTP_OK

usersDB = Users(db_path=DB_PATH)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    email, password = getargs(request, 'email', 'password')
    if not email or not password:
        return abort(401)
    exist = usersDB.getByEmail(email)
    if exist['code'] == 404:
        return HTTP_ERR(status=400, message='user does not exist')
    if exist['code'] != 200:
        return HTTP_ERR(status=500, message=exist['message'])
    if password_verification(password, exist['data']['password']):
        user = exist['data']
        return generate_auth_token(user)
    return HTTP_ERR(status=401, message='bad login')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('login/register.html')

    email, password = getargs(request, 'email', 'password')

    if not email or not password:
        return HTTP_ERR(message='parameter is missing', status=400)
    exist = usersDB.getByEmail(email)
    if exist['code'] == 200:
        return HTTP_ERR(message='user already exist by this email {}'.format(email), status=401)

    if exist['code'] != 404:
        return HTTP_ERR(message=exist['message'])
    data = {
        "email": email,
        "password": to_hash(password)
    }
    response = usersDB.save(data)
    if response['code'] != 200:
        return HTTP_ERR(message=response['message'])
    token = generate_auth_token(response['data'])
    return HTTP_OK(token=token.decode(), data=response['data'])


@app.route('/api/update_token')
@secured()
def updateToken():
    token_data = updateToken._token_data
    new_token = generate_auth_token(token_data)
    return new_token

