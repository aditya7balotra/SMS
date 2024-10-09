from . import adminDashBlu
from flask import render_template

@adminDashBlu.route('/')
def home():
    '''
    this view will redirect the admin to the admin's home page
    '''
    return render_template('dashboard_home.html')