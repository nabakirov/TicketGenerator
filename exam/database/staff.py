from .db import db


class Subject(db):
    def save(self, data):
        saveSQL = '''
            INSERT INTO Subjects(name)
            VALUES (?)
        '''
        name = data['name']
        self.create_conn()
        response = self.do(saveSQL, params=(name,), commit=True)
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

    def getList(self):
        sql = '''
            SELECT id, name FROM Subjects
        '''
        self.create_conn()
        raw = self.do(sql, out=True)
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
        return sList



