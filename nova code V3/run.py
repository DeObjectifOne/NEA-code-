# Import the create_app function from app.py
from website.app import create_app  

  # Create the Flask app
app = create_app()

 #Run the app in debug mode
 #this is so that any changes occur live
if __name__ == '__main__':
    app.run(debug=True) 
