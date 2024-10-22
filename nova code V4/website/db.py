import sqlite3
from flask import g
from os import path, makedirs

#creates the database
# done only if the database does not already exist
INSTANCE_FOLDER = path.join('website', 'instance')
DB_NAME = "database.db"
DB_PATH = path.join(INSTANCE_FOLDER, DB_NAME)

#creates a folder called instance inside the website folder
#done only if the instance does not already exist
makedirs(INSTANCE_FOLDER, exist_ok=True)

#function to connect to the SQLite database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

#function used to close the database function
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

#function to make the table
#only if it does not already exist
def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Create tasks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

#initializes the database
#allows it to run
def init_db():
    db = get_db()

    #code only for sql schemas
    #with open(path.join('website')) as f:
    #    db.executescript(f.read())