from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#creation of the database
db = SQLAlchemy()
DB_NAME = "database.db"


#used to both instantiate flask
def create_app():
     app = Flask(__name__)
     #A secret key is installed to encypt data to increase overall security
     app.secret_key = secrets.token_hex(24)
     app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
     db.init_app(app)

     #used to import code from auth.py and views.py
     from .views import views
     from .auth import auth

     #used tp return the roots/webpages tied to these specific python programs
     #is used so that any inputs made in html is translated into the python code
     app.register_blueprint(views, url_prefix='/')
     app.register_blueprint(auth, url_prefix='/')

     from .models import User, Task

     #used to create the database and its respective tables
     with app.app_context():
          db.create_all()

     #used to aknowledge that the user is logged in
     login_manager = LoginManager()
     login_manager.login_view = 'auth.login'

     login_manager.init_app(app)

     @login_manager.user_loader
     def load_user(id):
          return User.query.get(int(id))

     return app


#used to create a database if there isn't one already installed
def create_database(app):
     if not path.exists('website/' + DB_NAME):
          db.create_all(app=app)
          print("Database has been initialized")
