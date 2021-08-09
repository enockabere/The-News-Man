from flask import Flask
from config import config_options

def create_app(config_name):
    app = Flask(__name__)
    #creating the app configuration
    app.config.from_object(config_options[config_name])
    # will add views and forms
    from app import views
    from app import error
    return app
