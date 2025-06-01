# run.py

#! Mongo configs (create a .env and add a str MONGO_URI = "your mongo uri"  to run locally!!)

from app import create_app

# Create the flask app instance
app = create_app()

# run the app (debug mode)
if __name__ == '__main__':
    app.run(debug=True)
