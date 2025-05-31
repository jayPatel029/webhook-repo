# app/__init__.py

from flask import Flask
from .webhook.routes import webhook_bp
from flask_cors import CORS 


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(webhook_bp)
    return app
