from flask import Blueprint

# creating the blueprint for registration
loginBlu = Blueprint('loginBlu' , __name__ , template_folder='templates' , static_folder = 'static')
registerBlu = Blueprint('registerBlu' , __name__ , template_folder='templates' , static_folder = 'static')
# importing the routes and views for registration blueprint
from . import login_routes,register_routes