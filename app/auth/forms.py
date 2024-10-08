from flask_wtf import FlaskForm
# import email_validator
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    SubmitField , 
    EmailField , 
    SelectField , 
    FileField ,  
    IntegerField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Length,
    Regexp,
    EqualTo
)
# from flask_wtf.file import FileAllowed , FileRequired


class RegisterForm(FlaskForm):
    '''
    this is the registration form asking for the following details:
    1. institute name
    2. address of the institute
    3. email
    4. password
    5. confirm password
    5. contact number
    6. principal name
    7. school type
  
    8. agree to the terms and conditions
    9. submit button
    '''
    
    instituteName = StringField('Institute Name', validators=[DataRequired(), Length(min=1, max=50)])
    
    address = StringField('Address' , validators=[DataRequired()])
    
    email = EmailField('Email' , validators= [DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired() , EqualTo('password' , message = 'Passwords must be same')])
    
    
    contactNumber = StringField('Contact Number', validators=[
        DataRequired(),
        Regexp('^[0-9]{10}$', message="Invalid phone number. Must be 10 digits.")
    ])
    
    # contactNumber = IntegerField('Contact Number', validators= [DataRequired() , Length(min=10 , max=10)])
    
    principalName = StringField('Principal Name' , validators=[DataRequired()])
    
    schoolType = SelectField(
        'School Type' ,
        choices=[
        ('primary' , 'Primary'),
        ('secondary' , 'Secondary'),
        ('higherSecondary' , 'Higher Secondary')
        ],
        validators = [DataRequired()])
    
    # logo = FileField('Upload the logo of your school', validators=[
    #     FileRequired(message="File field cannot be empty."),
    #     FileAllowed(['jpg', 'png' , 'pdf'], 'Images only!')
    # ])
    
    agree = BooleanField('I agree to the terms and conditions' , validators=[DataRequired()])
    
    submit = SubmitField('Register')

class t_s_LoginForm(FlaskForm):
    userType = SelectField(
        'Are you' ,
        choices=[
        ('teacher' , 'Teacher'),
        ('student' , 'Student'),
        ],
        validators = [DataRequired()])
    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    remember_me=BooleanField(
        "Remember Me",
        validators= [DataRequired()]
    )
    submit=SubmitField("Login")
    
class adminLoginForm(FlaskForm):
    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    submit=SubmitField("Login")
