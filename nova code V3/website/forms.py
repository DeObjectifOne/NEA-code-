from flask import Blueprint, render_template, request, flash, redirect, url_for
from .db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

# Creates a blueprint called forms
forms = Blueprint('forms', __name__)

# Route used for the login page
@forms.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        db = get_db()
        cursor = db.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()

        if user:
            flash('Login successful!', category='success')
            # Redirect to another page or home after login
            return redirect(url_for('pages.home'))  # assuming you have a home page in 'pages'
        else:
            flash('Login failed. Check your email and password.', category='error')

    return render_template("login.html")

# Route used for the sign-up page
@forms.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email or password is empty
        if not email or not password:
            flash('Email and password cannot be empty', category='error')
        elif len(password) < 8:
            flash('Your password must be at least 8 characters long', category='error')
        else:
            db = get_db()
            cursor = db.execute("SELECT * FROM users WHERE email = ?", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Email already in use. Please log in instead.', category='error')
            else:
                # Correct hashing method with 'pbkdf2:sha256'
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                db.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
                db.commit()

                flash('Account created successfully', category='success')
                return redirect(url_for('forms.name'))
    return render_template("sign-up.html")

# Route used for the user to input their name
@forms.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')  # Assume user passes their email for reference

        db = get_db()
        cursor = db.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            db.execute("UPDATE users SET name = ? WHERE email = ?", (name, email))
            db.commit()
            flash('Name added successfully!', category='success')
            return redirect(url_for('pages.home'))  # Redirect to home page after name input

    return render_template("name.html")
