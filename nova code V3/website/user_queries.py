from db import get_db

#used to add a new user to the database
#it manually inserts the user's details into their respective values
def add_user(name, email, password):
    """A new user is added to the database"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO user (name, email, password)
        VALUES (?, ?, ?)
    """, (name, email, password))
    db.commit()

#retrieves the user's email
#this is for login purposes
#this is to see if the user is trying to input an already extant email
#if it returns with true, then the user is denied access
def get_user_by_email(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE email = ?
    """, (email, ))
    return cursor.fetchnone()

#user to delete a user
#this is done using their id
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM users WHERE id = ?
    """, (user_id, ))
    db.commit