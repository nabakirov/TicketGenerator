from docx import Document
import os
from exam.configs import FILES_PATH
from datetime import datetime



def getDoc(data):
    document = Document()
    for ticket in data['tickets']:
        document.add_heading('Билет № {}'.format(ticket['t_number']))
        for q in ticket['questions']:
            document.add_paragraph('\t{}. {}'.format(q['q_number'], q['text']))
        # document.add_paragraph('')
    file_dir = '{}/{}/{}'.format(FILES_PATH, data['user_id'], data['subject_id'])
    os.makedirs(file_dir, exist_ok=True)
    filename = '{}_{}_{}_{}_{}.docx'.format(data['user_id'], data['subject_id'], data['t_count'], data['q_count'], datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
    file_dir = file_dir + '/' + filename
    document.save(file_dir)
    return filename
