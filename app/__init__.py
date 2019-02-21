# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SECRET_KEY']="MYSECRETKEY"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "You must be logged in to access this page!!"


#registering all the blue prints...
from app import models
from app.admin import admin
from app.auth import auth
from app.home import home
from app.error_handler import error
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(error)




