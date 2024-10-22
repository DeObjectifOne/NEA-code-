from flask import Blueprint, render_template, request, flash, redirect, url_for, session
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

#route used for the logout function
@forms.route('/logout')
def logout():
    return "<p>logout</p>"

#function for the sign-up page
@forms.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #checks the input boxes to see if they're empty
        if not email or not password:
            flash('Email and password cannot be empty.', category='error')
            #checks if the user's password exceeds that of 8 characters
        elif len(password) < 8:
            flash('Your password must be at least 8 characters long.', category='error')
        else:
            #if these checks are complete, the database then fetches the free email slot
            #the user's inputted email will then fill this slot
            db = get_db()
            cursor = db.execute("SELECT * FROM users WHERE email = ?", (email,))
            existing_user = cursor.fetchone()

            #checks if the inputted email is extant
            if existing_user:
                flash('Email already in use. Please log in instead.', category='error')
            else:
                #the inputted password is hashed for increased security
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                db.execute(
                    #the password and email are then inputted into the database
                    "INSERT INTO users (email, password) VALUES (?, ?)",
                    (email, hashed_password)
                )
                db.commit()

                #Stores the user's email in the session
                session['email'] = email
                return redirect(url_for('forms.name'))

    return render_template("sign-up.html")


@forms.route('/name', methods=['GET', 'POST'])
def name():
    #The email from the previos session is retrieved
    #this ensures the user's name is tied to the email
    email = session.get('email')

    #if the email is unable to be linked, the user will be redirected back to the sign up page
    if not email:
        flash('Session expired or email not found. Please log in again.', category='error')
        return redirect(url_for('forms.sign_up'))

    if request.method == 'POST':
        name = request.form.get('name')

        #if the user fails to enter their name, the page will reload
        #it reloads with a flash message popping up
        if not name:
            flash('Please enter your name.', category='error')
            return render_template("name.html")

        #the user's name is then entered into the database
        db = get_db()
        db.execute("UPDATE users SET name = ? WHERE email = ?", (name, email))
        db.commit()

        flash('Name added successfully!', category='success')
        #once all the checks are complete, the user can then enter the home page
        return redirect(url_for('pages.home'))

    return render_template("name.html")
