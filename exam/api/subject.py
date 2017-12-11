from exam.database import Subject
from exam.configs import DB_PATH

subjectDB = Subject(db_path=DB_PATH)


class SubjectController:
    def save(self, data):
        response = subjectDB.save(data)
        return response

    def delete(self, id_):
        response = subjectDB.delete(id_)
        return response

    def update(self, data):
        response = subjectDB.update(data)
        return response

    def getListByUser_id(self, user_id):
        response = subjectDB.getListByUser_id(user_id)
        return response
