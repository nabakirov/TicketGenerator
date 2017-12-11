from exam.database import Question
from ..configs import DB_PATH



class Generate:
    def __init__(self, subject_id: int, user_id: int, ticket_cnt: int, q_cnt: int):
        self.db = Question(db_path=DB_PATH)
        self.subject_id = subject_id
        self.user_id = user_id
        self.make_ticket_cnt = ticket_cnt
        self.make_q_cnt = q_cnt
        self.getList()

    def getList(self):
        qList = self.db.getListBySubject_id(self.subject_id, self.user_id)
        if qList['code'] == 404:
            self.qList = None
        else:
            self.qList = qList['data']
            self.count = len(qList['data'])

    def getQlist(self):
        return self.qList

    def getTickets(self):
        if not self.qList:
            return dict(code=404, message='question list is empty')
        from random import choice
        tickets = []

        for i in range(1, self.make_ticket_cnt):
            q = []
            qList = self.getQlist()
            for j in range(1, self.make_q_cnt):

                randQ = choice(qList)
                print(i, j, qList)
                qList.remove(randQ)
                print(i, j, qList)
                q.append(
                    {
                        'q_number': j,
                        'text': randQ['text']
                    }
                )
            tickets.append(
                {
                    't_number': i,
                    'questions': q
                }
            )
        return dict(code=200, data=tickets)