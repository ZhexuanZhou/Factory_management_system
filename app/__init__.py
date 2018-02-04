from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)  # this must be in the front of blueprint import
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
login.session_protection = 'strong'

# This is actually a simple, yet frustrating issue. The problem is you are importing main
# BEFORE you are creating the instance of db in your __init__.py
from app.main import main
from app.api_routes import api
from app.auth_routes import auth

app.register_blueprint(main)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(auth, url_prefix='/auth')



from app import models
