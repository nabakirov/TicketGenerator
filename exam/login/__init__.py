from flask_login import UserMixin
from exam import login_manager
from .security import toHash, hashCompare
from ..configs import DB_PATH
from exam.database import Users

usersDB = Users(db_path=DB_PATH)

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    exist = usersDB.getByEmail(email)
    if exist['code'] != 200:
        return
    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    exist = usersDB.getByEmail(email)
    if exist['code'] != 200:
        return
    user = User()
    user.id = email
    user.is_authenticated = hashCompare(toHash(request.form['password']), exist['data']['password'])
    return user
