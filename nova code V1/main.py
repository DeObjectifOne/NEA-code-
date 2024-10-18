from website import create_app

app = create_app()

#used to run the app in debug mode
#this is so that changes can be made on the fly rather than having to restart the server
if __name__ == '__main__':
    app.run(debug=True)