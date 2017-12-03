from exam import app
from flask_login import login_required


@app.route('/<user_id>', methods=['GET'])
@login_required
def subject_list(user_id):
    pass


@app.route('/<user_id>/<subject_id>', methods=['GET'])
@login_required
def question_list(user_id, subject_id):
    pass


@app.route('/<user_id>/<subject_id>/<question_id>')
@login_required
def question(user_id, subject_id, question_id):
    pass