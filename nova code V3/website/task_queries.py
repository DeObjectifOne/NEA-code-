from db import get_db

#used to add a task to the database
#this task is user specific
#this is done through the user_id variable
def add_task(task_name, user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO tasks (task_name, user_id)
        VALUES (?, ?)
    """, (task_name, user_id))
    db.commit

#retrieves all the user's tasks
#these tasks are specific to them
def get_tasks_by_user(user_id):
    db = get_db
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM tasks WHERE user_id = ?
    """, (user_id,))
    return cursor.fetchall()

#retrieves all the user's tasks by ID
def get_task_by_id(task_id):
    db = get_db
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM tasks WHERE id = ?
    """ (task_id,))
    return cursor.fetchone()

#deletes user tasks
#finds them first by using the task id
#sqlite3 then performs a delete function on them
def delete_task(task_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM tasks WHERE id = ?
    """, (task_id, ))
    db.commit()