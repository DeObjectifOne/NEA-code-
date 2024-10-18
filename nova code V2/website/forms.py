from flask import Blueprint, render_template

#creates a blueprint called forms
#this can be imported elsewhere
forms = Blueprint('forms', __name__)

#route used for the login page
@forms.route('/login')
def login():
    return render_template("login.html")

#route used for the logout function
@forms.route('/logout')
def logout():
    return "<p>logout</p>"

#route used for the sign-up page
@forms.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

#route used for the user to input their name
@forms.route('/name')
def name():
    return render_template("name.html")


