from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

#used to create a WSGI (Web Server Gateway Interference) that handles user requests
from werkzeug.security import generate_password_hash, check_password_hash

#imports the database to store user data from login and sign up
from . import db

#used to handle data from the user
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#route used for the login function
@auth.route('/login', methods=['GET', 'POST'])
def login():
    #makes POST request to the server
    #it sends over the user inputted details
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #checks if the user entered email is a duplicate
        user = User.query.filter_by(email=email).first()
        if user:
            #checks if the user entered password exists in the database and is unique to the email
            if check_password_hash(user.password, password):
                flash('Login successful', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password incorrect, please try again', category='error')
        else:
            flash('The user does not exist, please input a different email',
                  category='error')

    #if all the checks are completed, the user will be redirected to the home page
    return render_template("login.html", user=current_user)


#route used for the logout function
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    #used to redirect the user back to the login page
    return redirect(url_for('auth.login'))


#route used for the sign up function
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #makes POST requests to the server
    #sends over all of the user's inputs
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #used to find if the user already exists in the database
        user = User.query.filter_by(email=email).first()
        #password validation
        #this forces the user to make their password more complicated
        #this is to increase overall user security
        if user:
            flash(
                'A user with this email already exists, please input a different email',
                category='error')
        elif len(password1) < 8:
            flash('The password length cannot be shorter than 8 characters',
                  category='error')
        elif password1 != password2:
            flash('The passwords do not match', category='error')
        elif not password1.isalnum():
            flash('Passowrd must contain letters and numbers',
                  category='error')
        elif not password1.isalpha():
            flash('Password must contain letters', category='error')
        else:
            #once the user has passed all these checks, their details are stored in the database
            #the user is then granted access to the website
            new_user = User(email=email,
                            fullname=fullname,
                            password=generate_password_hash(
                                password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Accounted created successfully', category='success')
            return redirect(url_for('views.home'))
    #the user is then sent to the home page
    return render_template("sign-up.html", user=current_user)
