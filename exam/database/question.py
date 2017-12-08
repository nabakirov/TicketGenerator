from .db import db

class Question(db):
    def save(self, data):
        sql = '''
            insert into Questions(
                user_id,
                subject_id,
                title,
                text,
                hardness,
                uploaded)
            values(?, ?, ?, ?, ?, ?)
        '''
        params = (data['user_id'], data['subject_id'], data['title'], data['text'], data['hardness'], data['uploaded'])
        self.create_conn()
        sql_response = self.do(sql, params=params, commit=True)
        self.close_conn()
        return sql_response

    def update(self, data):
        sql = '''
            update Questions set
                subject_id = ?,
                title = ?,
                text = ?,
                hardness = ?
            where id = ?
        '''
        params = (data['subject_id'], data['title'], data['text'], data['hardness'], data['id'])
        self.create_conn()
        sql_response = self.do(sql, params=params, commit=True)
        self.close_conn()
        return sql_response

    def delete(self, id):
        sql = '''
            delete from Questions
            where id = ?
        '''
        self.create_conn()
        sql_response = self.do(sql, params=(id,), commit=True)
        self.close_conn()
        return sql_response

    def getListBySubject_id(self, subject_id, user_id):
        sql = '''
            select
                id,
                user_id,
                subject_id,
                title,
                text,
                hardness,
                uploaded
            from Questions
            where
                subject_id = ?
            and user_id = ?
        '''
        self.create_conn()
        sql_response = self.do(sql, params=(subject_id, user_id), out=True)
        self.close_conn()
        if sql_response['code'] == 404:
            return dict(code=404, message='question list is empty')
        if sql_response['code'] != 200:
            return sql_response
        response = []
        for qs in sql_response['data']:
            response.append({
                'id': qs[0],
                'user_id': qs[1],
                'subject_id': qs[2],
                'title': qs[3],
                'text': qs[4],
                'hardness': qs[5],
                'uploaded': qs[6]
            })
        return dict(code=200, data=response)




