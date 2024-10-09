from flask import Blueprint

# registering the blueprint with name 'adminDashBlu'
adminDashBlu = Blueprint('adminDashBlu' , __name__, template_folder= 'templates', static_folder= 'static')


# importing the routes
from . import dashboard_routes

