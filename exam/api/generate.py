from exam.database import Question
from ..configs import DB_PATH
from .exportDoc import getDoc


class Generate:
    def __init__(self, subject_id: int, user_id: int, ticket_cnt: int, q_cnt: int, header=None, footer=None):
        self.db = Question(db_path=DB_PATH)
        self.subject_id = subject_id
        self.user_id = user_id
        self.make_ticket_cnt = ticket_cnt
        self.make_q_cnt = q_cnt
        self.header = header
        self.footer = footer
        self.getList()

    def getList(self):
        qList = self.db.getListBySubject_id(self.subject_id, self.user_id)
        if qList['code'] == 404:
            self.qList = None
        else:
            self.qList = qList['data']
            self.count = len(qList['data'])
        return qList['data']



    def getTickets(self):
        if not self.qList:
            return dict(code=404, message='question list is empty')
        from random import choice
        tickets = []

        for i in range(1, self.make_ticket_cnt + 1):
            q = []

            qList = self.qList[:]

            for j in range(1, self.make_q_cnt + 1):

                randQ = choice(qList)
                qList.remove(randQ)
                q.append(
                    {
                        'q_number': j,
                        'text': randQ['text'],
                        'hardness': randQ['hardness']
                    }
                )
            tickets.append(
                {
                    't_number': i,
                    'questions': q
                }
            )
        data = {
            "tickets": tickets,
            "t_count": self.make_ticket_cnt,
            "q_count": self.make_q_cnt,
            "user_id": self.user_id,
            "subject_id": self.subject_id,
            "header": self.header,
            "footer": self.footer
        }
        filename = getDoc(data)
        data['filename'] = filename
        return dict(code=200, data=data)