# creating the database ---> clients
import mysql.connector
from dotenv import load_dotenv
import os


#loading env variables
load_dotenv()

# clients database script path
clients_file = 'models/clients.sql'

def establish_clients_db():
    # Establishing the connection with the clients database
    # sup_conn => super connection (connection for super admins database (clients), we)
    sup_conn = mysql.connector.connect(
        host=os.getenv('db_host'),
        user=os.getenv('db_username'),
        password=os.getenv('db_pswd'),
        # database = 'my_sms'
    )

    sup_cursor = sup_conn.cursor()

    # Execute the SQL file
    with open(clients_file, 'r') as file:
        content = file.read()
        
    for i in sup_cursor.execute(content , multi = True):
        pass

    # commit the changes
    sup_conn.commit()

    # closing the connection
    sup_conn.close()
    
    return 'database successfully established'



# creating the connection pooling for the clients database
sup_connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="sup_pool",
    pool_size=5,  # Size of the pool, adjust based on traffic
    pool_reset_session=True,  # Resets session for new connections
    host=os.getenv('db_host'),
    database='clients',
    user=os.getenv('db_username'),
    password=os.getenv('db_pswd')
)





