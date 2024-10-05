import bcrypt
import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1931",
        database="clients"
    )
def hash_password(plain_password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password
email=input("Enter a email: ")
plain_password=input("Enter a pass: ")
hashed_password = hash_password(plain_password)
conn = get_db_connection()
cursor = conn.cursor()
query = "INSERT INTO users (email, password) VALUES (%s, %s)"
cursor.execute(query, (email, hashed_password))
conn.commit()
cursor.close()
conn.close()