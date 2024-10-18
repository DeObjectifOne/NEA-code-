from flask import Flask, render_template

#function used for running the app
#later imported to run.py
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sykjdshdg'

    #imports all routes from forms.py
    #imports all routes from pages.py
    from .forms import forms
    from .pages import pages

    #these routes can then be run by run.py
    app.register_blueprint(forms, url_prefix='/')
    app.register_blueprint(pages, url_prefix='/')

    #completes the function
    #sends it over to run.py
    return app