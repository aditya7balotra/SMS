from flask import render_template , request , session , redirect,url_for
from .forms import t_s_LoginForm , adminLoginForm
import mysql.connector
from . import loginBlu
import bcrypt
from ..middleware import auth,guest
from models import sup_connection_pool
import os

def get_db_connection():
    connection = sup_connection_pool.get_connection()
    return connection

def prevent_cache(response):
    """Prevent the browser from caching the page to block back button navigation."""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@loginBlu.route('/',methods = ['GET','POST'])
@guest
def login_user():
    '''
    this view is going to register the details of the user in our database
    '''
    t_s_Form = t_s_LoginForm()
    adminForm = adminLoginForm()
    
    if adminForm.validate_on_submit():
        # this will run as the user will submit the admin login form
        # print("sucessfully")
        
        # fetch the details
        email = adminForm.email.data
        plain_password = adminForm.password.data
        
        # search in the database
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT passwords FROM auth WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        
        # closing connection
        cursor.close()
        conn.close()
        
        if result:
            # print(result)
            hashed_password = result[0]
            # salt = bcrypt.gensalt()
            
            if bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8')):
                # this will run if the hashed password matches
                # saving to session
                # session['email'] = email
                # session['password']=plain_password
                # print('redirecting to the dashboard')
                return 'WELCOME TO THE DASHBOARD'
        
            else:
                return "Invalid email or password"
        else:
            return "Email not found."
    
    elif t_s_Form.validate_on_submit():
        # this will run if any teacher or student fills the form
        email = t_s_Form.email.data
        plain_password = t_s_Form.password.data
        
        return 'THIS PAGE IS YET TO BUILD'

        
    return render_template('login.html' , t_s_form =t_s_Form , adminform = adminForm)
    
