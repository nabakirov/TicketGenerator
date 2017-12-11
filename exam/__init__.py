from flask import Flask

app = Flask(__name__,
            static_url_path='/static',
            static_folder='../web/static',
            template_folder='../web/templates')
app.secret_key = 'QWERTY'


from .views import *
from .security import *
