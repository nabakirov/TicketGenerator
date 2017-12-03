from flask import Flask
import flask_login


app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

app.secret_key = 'QWERTY'


from .views import *
