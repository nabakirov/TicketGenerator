from flask import Flask



app = Flask(__name__)
app.secret_key = 'QWERTY'


from .views import *
from .security import *