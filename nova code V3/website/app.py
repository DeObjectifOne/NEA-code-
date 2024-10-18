from flask import Flask, render_template
from .db import create_database, get_db, close_db
from .user_queries import add_user, get_user_by_email
from .task_queries import add_task, get_tasks_by_user

#function used for running the app
#later imported to run.py
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sykjdshdg'

    #instansiates the database
    create_database()

    #imports all routes from forms.py
    #imports all routes from pages.py
    from .forms import forms
    from .pages import pages

    #these routes can then be run by run.py
    app.register_blueprint(forms, url_prefix='/')
    app.register_blueprint(pages, url_prefix='/')

    #teardown function
    #used to close the database when it has fully connected
    app.teardown_appcontext(close_db)

    #attaches the user and task functions to the app context
    #this is so all the functions from there are imported to here
    app.add_url_rule('/add_user', 'add_user', add_user)
    app.add_url_rule('/add_task', 'add_task', add_task)
    app.add_url_rule('/get_tasks/<int:user.id>', 'get_tasks_by_user', get_tasks_by_user)

    #completes the function
    #sends it over to run.py
    return app