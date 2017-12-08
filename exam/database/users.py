from .db import db
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from exam.configs import SECRET_KEY

class Users(db):
    @staticmethod
    def parse(raw):
        return dict(
            id=raw[0],
            email=raw[1],
            password=raw[2]
        )

    def save(self, data):
        sql = '''
            INSERT INTO Users(email, password)
            VALUES (?, ?)
        '''
        sql_select = '''
        select id, email, password from users
        where email = ?
        '''
        params = (data['email'], data['password'])
        self.create_conn()
        response = self.do(sql, params=params, commit=True)
        if response['code'] != 200:
            self.close_conn()
            return response
        response = self.do(sql_select, params=(data['email'],), out=True)
        self.close_conn()
        if response['code'] != 200:
            return response
        return dict(code=200, data=dict(data=self.parse(response['data'][0])))

    def getByEmail(self, email):
        sql = '''
            SELECT id, email, password FROM Users
            WHERE email = ?
        '''
        self.create_conn()
        response = self.do(sql, params=(email,), out=True)
        self.close_conn()

        if response['code'] == 404:
            return dict(code=404, message='User not found')
        if response['code'] != 200:
            return response
        response = response['data'][0]
        user = {
            "id": response[0],
            "email": response[1],
            "password": response[2]
        }
        return dict(code=200, data=user)

    def getList(self):
        sql = '''
            SELECT id, email, password FROM Users
        '''
        self.create_conn()
        response = self.do(sql, out=True)
        self.close_conn()

        if response['code'] == 404:
            return dict(code=404, message='there is no users')
        if response['code'] != 200:
            return response
        userslist = []
        for user in response['data']:
            userslist.append({
                "id": user[0],
                "email": user[1],
                "password": user[2]
            })
        return dict(code=200, data=userslist)


class User:
    id = None
    email = None

    def __init__(self, email, pwd):
        self.email = email
        self.password_hash = pwd_context.encrypt(pwd)



    def verify_password(self, pwd):
        return pwd_context.verify(pwd, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({"id": self.id,
                        "email": self.email})