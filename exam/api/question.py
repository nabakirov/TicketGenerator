from exam.database import Question
from exam.configs import DB_PATH
from time import time as now

questionDB = Question(db_path=DB_PATH)


class QuestionController:
    def save(self, data):
        data['uploaded'] = now()
        response = questionDB.save(data)
        return response

    def delete(self, id_):
        response = questionDB.delete(id_)
        return response

    def update(self, data):
        response = questionDB.update(data)
        return response

    def getListBySubject_id(self, subject_id):
        response = questionDB.getListBySubject_id(subject_id)
        return response
