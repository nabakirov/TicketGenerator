from .db import db


class Subject(db):
    def save(self, data):
        saveSQL = '''
            INSERT INTO Subjects(name, user_id)
            VALUES (?, ?)
        '''
        params = (data['name'], data['user_id'])
        self.create_conn()
        response = self.do(saveSQL, params=params, commit=True)
        self.close_conn()
        return response

    def update(self, data):
        updateSQL = '''
            UPDATE Subjects SET
                name = ?
            WHERE
                id = ?
        '''
        params = (data['name'], data['id'])
        self.create_conn()
        response = self.do(updateSQL, params=params, commit=True)
        self.close_conn()
        return response

    def delete(self, id_):
        delSQL = '''
            DELETE FROM Subjects
            WHERE id = ?
        '''
        self.close_conn()
        response = self.do(delSQL, params=(id_,), commit=True)
        self.close_conn()
        return response

    def getListByUser_id(self, user_id):
        sql = '''
            SELECT id, name FROM Subjects
            Where user_id = ?
        '''
        self.create_conn()
        raw = self.do(sql, params=(user_id,), out=True)
        self.close_conn()
        if raw['code'] == 404:
            return dict(code=404, message='list is empty')
        if raw['code'] != 200:
            return raw
        sList = []
        for subject in raw['data']:
            sList.append({
                'id': subject[0],
                'name': subject[1]
            })
        return dict(code=200, data=sList)

