from flask import Blueprint

# creating the blueprint for registration
registerBlu = Blueprint('registerBlu' , __name__ , template_folder='templates' , static_folder = 'static')

# importing the routes and views for registration blueprint
from . import register_routes