from .db import db


class Users(db):
    def save(self, data):
        sql = '''
            INSERT INTO Users(email, password)
            VALUES (?, ?)
        '''
        params = (data['email'], data['password'])
        self.create_conn()
        response = self.do(sql, params=params, commit=True)
        self.close_conn()
        return response

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
