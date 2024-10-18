from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Task
from . import db
import json
from .csv_utils import read_tasks_from_csv, write_task_to_csv

views = Blueprint('views', __name__)

from flask_login import current_user

@views.context_processor
def inject_user():
    return {'user': current_user}

# Route for the home page
@views.route('/', methods=['GET', 'POST'])
@login_required  # Requires the user to be logged in
def home():
    if request.method == 'POST':
        # Retrieve the task from the form
        task = request.form.get('task')
        if task:  # Check if task is not empty
            # Create a new task and associate it with the current user
            new_task = Task(data=task, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('Task added successfully', category='success')
        else:
            flash('Task cannot be empty', category='error')

    # Render the homepage and pass the current user
    return render_template("home.html", user=current_user)


# Route for handling task deletion via POST request
@views.route('/delete-task', methods=['POST'])
def delete_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Task.query.get(taskId)
    
    if task:
        # Ensure the task belongs to the current user before deleting
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
            flash('Task deleted successfully', category='success')
        else:
            flash('Unauthorized action', category='error')
    
    return jsonify({})  # Return an empty response as JSON


# Dashboard route for viewing tasks from the CSV file
@views.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', tasks=tasks, user=current_user)


# Route for searching tasks by query
@views.route('/search', methods=['POST'])
@login_required
def search():
    query = request.form.get('query', '').lower()
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', tasks=tasks, query=query)



# Route for adding a task via CSV
@views.route('/add_task', methods=['POST'])
@login_required
def add_task():
    task_data = request.form.get('task')
    if task_data:
        user_id = current_user.id
        write_task_to_csv(task_data, user_id)  # Write task to CSV
        flash('Task added to CSV successfully', category='success')
    else:
        flash('Task cannot be empty', category='error')
    
    return redirect(url_for('views.dashboard'))
