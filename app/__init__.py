# importing necessities

from flask import Flask,Blueprint,render_template
from .auth import loginBlu,registerBlu
from .profile import dashBlu
from .home import homeBlu
from models import establish_clients_db
from config import development_config
from dotenv import load_dotenv
import os

# loading the env variables
load_dotenv()

# establishing the clients db
establish_clients_db()

# creating the app object
app = Flask(__name__)

# app.config['SECRET_KEY']
app.config.from_object(development_config)

# Configure upload folder and allowed extensions


# list of all ready blueprints
# (blueprint_object , /url_prefix)
blueprints_list = [

    (loginBlu , '/login'),
    (registerBlu , '/register'),
    (dashBlu,'/dashboard'),
    (homeBlu,'/')

]

for blueprints in blueprints_list:
    # registering all the listed blueprints
    app.register_blueprint(blueprints[0] , url_prefix = blueprints[1])
    

def createApp():
    '''
    returning the app object
    '''
    return app