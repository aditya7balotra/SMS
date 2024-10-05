import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()


def send_mail(subject , body , to_email , password= os.getenv('email_pswd') , from_email = os.getenv('email')):
    
    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send the email
    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Start TLS encryption
            server.starttls()
            # Log in to your email account
            server.login(from_email, password)
            # Send the email
            server.send_message(msg)
            return 'email send successfully'
        
    except Exception as e:
        return f"email can't be sent :, {e}"
