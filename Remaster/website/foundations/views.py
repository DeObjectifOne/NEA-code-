from flask import Blueprint, render_template
from . import db
from models.task import Task

views = Blueprint('views', __name__)

@views.route('/')
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

@views.route('/settings')
def settings():
    return render_template('settings.html')
