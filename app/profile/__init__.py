from flask import Blueprint

# creating the blueprint for registration
dashBlu = Blueprint('dashBlu' , __name__ , template_folder='templates' , static_folder = 'static')

# importing the routes and views for registration blueprint
from . import dashboard_routes