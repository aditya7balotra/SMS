from flask import request,session
import mysql.connector
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1931",
        database="clients"
    )

# Custom session handler class
class MySQLSessionInterface:
    def open_session(self, app, request):
        session_id = request.cookies.get(app.session_cookie_name)

        if not session_id:
            session_id = str(uuid.uuid4())  # Generate a new session ID
            return self.new_session(session_id)

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT session_data, session_expiration FROM sessions WHERE session_id = %s", (session_id,))
        session_row = cursor.fetchone()
        db.close()

        if session_row and session_row['session_expiration'] > datetime.now():
            # If session is valid, load the session data
            return self.deserialize_session(session_id, session_row['session_data'])
        else:
            # If no session found or expired, create a new session
            return self.new_session(session_id)

    def new_session(self, session_id):
        return {'session_id': session_id, 'data': {}}

    def deserialize_session(self, session_id, session_data):
        return {'session_id': session_id, 'data': eval(session_data)}  # Simple eval, but can be improved

    def save_session(self, app, session, response):
        session_data = str(session['data'])  # Serialize session data
        session_id = session['session_id']
        session_expiration = datetime.now() + timedelta(hours=1)  # Set session expiration to 1 hour

        db = get_db_connection()
        cursor = db.cursor()

        # Insert or update session data in the database
        cursor.execute("""
            INSERT INTO sessions (session_id, session_data, session_expiration)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE session_data=%s, session_expiration=%s
        """, (session_id, session_data, session_expiration, session_data, session_expiration))
        db.commit()
        db.close()

        # Set session cookie in the response
        response.set_cookie(app.session_cookie_name, session_id, max_age=3600)

# Attach the custom session handler to Flask
app.session_interface = MySQLSessionInterface()
