# app/__init__.py

from flask import Flask
from .webhook.routes import webhook_bp
from flask_cors import CORS 


# config and create the app
def create_app():
    app = Flask(__name__)
    CORS(app) # enable cors
    app.register_blueprint(webhook_bp) # register webhook blueprint
    return app
