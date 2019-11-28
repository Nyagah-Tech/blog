from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create _app(config_name):
    app = Flask(__name__)

    # creating the app configuration
    app.config.from_object(config_options[config_name])

    # intilizing flask extensions
    bootstrap.init_app(app)

    # configure uploadset


    # register the blueprint


    return app
