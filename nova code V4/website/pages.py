from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)

#route used for the home page
@pages.route('/')
def home():
    return render_template("home.html")

#route used for the settings page
@pages.route('/settings')
def settings():
    return render_template("settings.html")