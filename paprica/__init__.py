from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///paprica.db"
app.config["SECRET_KEY"] = '8697d8a1ec77e8c9b434ae5a'

import os
from werkzeug.utils import secure_filename

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'paprica/static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "page_login"

# ⬇️ IMPORTA MODELS PRIMEIRO
from paprica.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ⬇️ IMPORTA BLUEPRINT SÓ DEPOIS QUE DB E MODELS EXISTEM
from paprica.admin_rotes import admin
app.register_blueprint(admin)

# ⬇️ POR ÚLTIMO IMPORTA ROUTES
from paprica import routes
