from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Task
from . import db
import json

views = Blueprint('views', __name__)

#used redirect the user to the default page (home page)
@views.route('/', methods=['GET', 'POST'])
@login_required  #put in place so the user can't access the home page until they've logged in
def home():
    if request.method == 'POST':
        #used to retrieve the task model and its respecive elements
        task = request.form.get('task')
        #a new task is then created with the help of the model
        #the task is also made unique to the user
        new_task = Task(data=task, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', category='success')
    #the homepage is then updated accordingly
    return render_template("home.html", user=current_user)

#handles task deletion after the user sends a POST request
@views.route('/delete-task', methods=['POST'])
def delete_task():
    #the JSON string from the JavaScript function is parsed
    #this means that its converted into a Python object
    #the function then locates the requested object to be deleted
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Task.query.get(taskId)
    if task:
        #this makes sure that the task.user_id and the current_user.id are the same before deleting the task
        #the associated details with the task are then removed from the database
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
    #the request is then serialized into JSON to be completed
    return jsonify({})

WORDS = []
with views("large", "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())