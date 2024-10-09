from flask import render_template , request , session , flash, redirect, url_for
from .forms import RegisterForm
from datetime import datetime
# importing the 'registration' blueprint
from . import registerBlu
import os
from models import sup_connection_pool
from app.passwords import gen_hash
import random
from app.send_mails import send_mail



@registerBlu.route('/' , methods = ['GET' , 'POST'])
def register_user():
    '''
    this view is going to register the details of the user in our database
    '''
    regForm = RegisterForm()
    
    if regForm.validate_on_submit():
        # fetch the details
        instituteName = regForm.instituteName.data
        address = regForm.address.data
        email = regForm.email.data
        password = regForm.password.data
        contactNumber = regForm.contactNumber.data
        principalName = regForm.principalName.data
        schoolType = regForm.schoolType.data
        # logo = regForm.logo.data
        # logo_name = secure_filename(logo.filename)
        # logo_path = f'app/static/uploads/logo/{instituteName}_{email}.{logo_name[-3:]}'
        # agree = regForm.agree.data
        
        
        # saving to session
        session['form_data'] = {
            'instituteName' : instituteName,
            'address' : address,
            'email' : email,
            'password' : password,
            'contactNumber' : contactNumber,
            'principalName' : principalName,
            'schoolType' : schoolType,
            # 'logo_path' : logo_path
        }
        
        # generating otp
        
        otp = random.randint(1000 , 9999)
        session['otp'] = str(otp)
        print(otp)
        
        # sending mail
        email_status = send_mail(
            subject= 'SMS registration OTP',
            body = f'Your registration OTP is {otp}',
            to_email= email
        )
        print(email_status)
        
        
        return render_template('otp.html')
    
        
    
    
        
    return render_template('register.html' , form = regForm)
    
    
@registerBlu.route('/otp' , methods = ['post'])
def verify_otp():

    otp = request.form.get('otp')
    if session['otp'] == otp:
        # saving info to the database
        data = session.get('form_data')
        
        query = '''
        INSERT INTO registered
        (instituteName , address , email , contactNumber , principalName , schoolType, date)
        VALUES
        (%s , %s , %s , %s , %s , %s , %s )
        '''
        values = (data['instituteName'], data['address'] , data['email'] , data['contactNumber'] , data['principalName'] , data['schoolType'] , datetime.now())
        sup_conn = sup_connection_pool.get_connection()
        sup_cursor = sup_conn.cursor()
        
        # executing the query in the database
        sup_cursor.execute(query , values)
        # saving the logo
        # data['logo'].save(data['logo_path'])
        # commiting the changes
        query = '''
        INSERT INTO auth 
        (email , passwords)
        VALUES
        (%s , %s)
        '''
        values = (data['email'] , gen_hash(data['password']))
        # saving the hashed password to the database
        sup_cursor.execute(query , values)
        
        # commiting and closing
        sup_conn.commit()
        
        sup_cursor.close()
        sup_conn.close()
        
        # removing form details and otp from the session
        session.pop('form_data' , None)
        session.pop('otp' , None)
        
        
        
        # redirecting the user to the login page after successfull registration
        return redirect('/')
    
    else:
        
        flash('Wrong OTP' , 'fail')
        return render_template('otp.html')
    

@registerBlu.route('/resendOTP')
def resendOTP():
    '''
    this view will recreate the OTP and send it to the user
    '''
    
    # fetching the email
    email = session.get('form_data').get('email')
    
    
    # generating otp
        
    otp = random.randint(1000 , 9999)
    session['otp'] = str(otp)
    print(otp)
    
    # sending mail
    email_status = send_mail(
        subject= 'SMS registration OTP',
        body = f'Your registration OTP is {otp}',
        to_email= email
    )
    
    print(email_status)
    
    return render_template('otp.html')
