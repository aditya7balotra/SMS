from flask import Blueprint

# creating the blueprint for registration
homeBlu = Blueprint('homeBlu' , __name__ , template_folder='templates' , static_folder = 'static')

# importing the routes and views for registration blueprint
from . import home_routes