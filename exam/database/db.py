
import sqlite3


class db:
    sql_path = None
    sql_connection = None
    db_path = None

    def __init__(self, sql_path=None, db_path=None):
        self.sql_path = sql_path
        self.db_path = db_path

    def create_conn(self):
        if self.sql_connection != None:
            return
        if self.db_path:
            try:
                conn = sqlite3.connect(self.db_path)
                self.sql_connection = conn
            except:
                self.sql_connection = None


    def close_conn(self):
        if self.sql_connection != None:
            self.sql_connection.close()
            self.sql_connection = None

    def do(self, query, executemany=False,  params=None, out=False, commit=False):
        conn = self.sql_connection
        if not conn:
            return dict(code=500, message='open connection first')
        cursor = self.sql_connection.cursor()
        if params:
            if executemany:
                cursor.executemany(query, params)
            else:
                cursor.execute(query, params)
        else:
            cursor.execute(query)
        if out:
            fetched = cursor.fetchall()
            if fetched.__len__() == 0:
                data = dict(code=404, message='data not found')
            else:
                data = dict(code=200, data=fetched)
        else:
            data = dict(code=200)
        if commit:
            conn.commit()
        cursor.close()
        return data

