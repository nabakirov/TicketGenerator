from exam import app
from flask import request, jsonify, g, render_template
from exam.api import SubjectController, QuestionController
from exam.utils import HTTP_ERR, HTTP_OK, getargs
from exam.security import secured
from flask import send_from_directory
import os
from exam.configs import FILES_PATH

subjectAPI = SubjectController()
questionAPI = QuestionController()


@app.route('/api/<user_id>', methods=['GET', 'POST'])
@secured()
def subject_list(user_id):
    token_data = subject_list._token_data
    tokenUserId = token_data.get('id')

    try:
        user_id = int(user_id)
    except:
        return HTTP_ERR(status=400, message='bad user id')
    if tokenUserId != user_id:
        return HTTP_ERR(status=401, message='unauthorized')
    if request.method == 'GET':
        sList = subjectAPI.getListByUser_id(user_id)
        if sList['code'] != 200:

            return HTTP_ERR(status=sList['code'], message=sList['message'])
        return HTTP_OK(data=sList['data'])
    id_, name = getargs(request, 'id', 'name')
    if not name:
        return HTTP_ERR(status=400, message='parameters is missing')
    data = dict(
        name=name,
        user_id=user_id
    )
    if id_:
        data['id'] = id_
        response = subjectAPI.update(data)
        if response['code'] != 200:
            return HTTP_ERR(status=response['code'], message=response['message'])
        return HTTP_OK()
    response = subjectAPI.save(data)
    if response['code'] != 200:
        return HTTP_ERR(status=response['code'], message=response['message'])
    return HTTP_OK()


@app.route('/api/<user_id>/<subject_id>', methods=['GET', 'POST'])
@secured()
def question_list(user_id, subject_id):
    token_data = question_list._token_data
    tokenUserId = token_data.get('id')
    if tokenUserId != int(user_id):
        return HTTP_ERR(status=401, message='unauthorized')
    if request.method == 'GET':
        qList = questionAPI.getListBySubject_id(subject_id, user_id)
        if qList['code'] != 200:
            return HTTP_ERR(status=qList['code'], message=qList['message'])
        return HTTP_OK(data=qList['data'])
    if request.method == 'POST':
        text, hardness, id_ = getargs(request, 'text', 'hardness', 'id')
        if not text or not hardness:
            return HTTP_ERR(message='parameter is missing', status=400)
        data = dict(
            text=text,
            hardness=hardness,
            user_id=user_id,
            subject_id=subject_id
        )
        if id_:
            data['id'] = id_
            response = questionAPI.update(data)
            return HTTP_OK(data=response)
        response = questionAPI.save(data)
        return HTTP_OK(data=response)


from exam.api import Generate


@app.route('/api/generate/<user_id>/<subject_id>', methods=['POST'])
@secured()
def generate_handler(user_id, subject_id):
    token_data = generate_handler._token_data
    tokenUserId = token_data.get('id')
    if tokenUserId != int(user_id):
        return HTTP_ERR(status=401, message='UNAUTHORIZED')
    ticket_cnt, q_cnt = getargs(request, 'ticket_cnt', 'question_cnt')
    if not ticket_cnt or not q_cnt:
        return HTTP_ERR(status=400, message='BAD REQUEST')
    try:
        ticket_cnt = int(ticket_cnt)
        q_cnt = int(q_cnt)
    except:
        return HTTP_ERR(status=400, message='parameters must be integer')
    generate = Generate(subject_id, user_id, ticket_cnt, q_cnt)
    if q_cnt > generate.count:
        return HTTP_ERR(status=400, message='can only make {} questions per ticket'.format(generate.count))
    tickets = generate.getTickets()
    if tickets['code'] != 200:
        return HTTP_ERR(status=tickets['code'], message=tickets['message'])
    filename = tickets['data']['filename']
    del tickets['data']['filename']
    return HTTP_OK(data=tickets['data'], filename=filename, download='/api/download?filename='+filename)


@app.route('/api/download', methods=['POST', 'GET'])
@secured()
def downloadHandler():
    token_data = downloadHandler._token_data
    tokenUserId = token_data.get('id')
    filename = getargs(request, 'filename')[0]
    if not filename:
        return HTTP_ERR(status=400, message='file path required')
    user_id, subject_id, tcnt, qcnt, date = filename.split('_')
    if tokenUserId != int(user_id):
        return HTTP_ERR(status=401, message='UNAUTHORIZED')
    directory = "{}/{}/{}".format(FILES_PATH, user_id, subject_id)
    if not os.path.isfile(directory + '/' + filename):
        return HTTP_ERR(status=400, message='File Does Not Exists')
    
    path = os.path.abspath(directory)
    print(path, filename)
    return send_from_directory(path, filename)
    
