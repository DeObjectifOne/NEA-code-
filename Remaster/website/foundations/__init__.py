from flask import Flask
from utilities.db import db
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'f09erh2-1d'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.../data/database.db'

    db.init_app(app)
    login_manager.init_app(app)

    from .views import views
    app.register_blueprint(views)

    with app.app_context():
        db.create_all()

    return app
