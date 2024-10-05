from flask import render_template,request
from . import dashBlu
from ..middleware import auth
@dashBlu.route('/',methods=['GET'])
@auth
def dash_admin():
    return render_template('dashboard.html')