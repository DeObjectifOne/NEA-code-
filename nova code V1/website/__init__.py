from flask import Flask
import secrets
from os import path
from flask_login import LoginManager
from .models import Task, User
from .db import db  # Import db from db.py

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the db with the app
    db.init_app(app)

    # Register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Create the database and its respective tables
    with app.app_context():
        db.create_all()

    # Login manager setup
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

