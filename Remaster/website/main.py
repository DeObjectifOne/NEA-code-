from website import create_app

#imports __init__.py to here to be run
app = create_app()

#the app is run in debug mode
#its so that any changes made update the app in real time
if __name__ == '__main__':
    app.run(debug=True)