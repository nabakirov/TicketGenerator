from exam import app
from flask import request, jsonify, g, render_template
from exam.api import SubjectController, QuestionController


subjectAPI = SubjectController()
questionAPI = QuestionController()


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/<user_id>', methods=['GET', 'POST'])

# @login_required
def subject_list(user_id):
    print(g.user)
    if request.method == 'GET':
        sList = subjectAPI.getListByUser_id(user_id)
        if sList['code'] != 200:
            return sList['message']
        return jsonify(sList['data'])
    try:
        data = request.get_json(force=True)
    except:
        return 'bad request'
    requirements = ['name', 'user_id']
    for require in requirements:
        if require not in data:
            return '{} is missing'.format(require)
    if 'id' in data:
        response = subjectAPI.update(data)
        return jsonify(response)
    response = subjectAPI.save(data)
    return jsonify(response)


@app.route('/<user_id>/<subject_id>', methods=['GET', 'POST'])

def question_list(user_id, subject_id):
    if request.method == 'GET':
        qList = questionAPI.getListBySubject_id(subject_id)
        if qList['code'] != 200:
            return qList['message']
        return jsonify(qList['data'])
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
        except:
            return 'bad request'
        requirements = ['user_id', 'subject_id', 'text', 'hardness']
        for require in requirements:
            if require not in data:
                return '{} is missing'.format(require)

        if 'id' in data:
            response = questionAPI.update(data)
            return jsonify(response)
        response = questionAPI.save(data)
        return jsonify(response)



@app.route('/<user_id>/<subject_id>/<question_id>', methods=['GET', 'POST'])

def question(user_id, subject_id, question_id):
    if request.method == 'GET':
        response = questionAPI.getListBySubject_id()
        pass
    else:
        # update question info
        pass


