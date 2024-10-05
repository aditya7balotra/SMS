import bcrypt

def gen_hash(pswd):
    # generate a salt
    salt = bcrypt.gensalt()
    
    # hash the password using the salt
    hashed_pswd = bcrypt.hashpw(pswd.encode('utf-8'), salt)
    
    return hashed_pswd
def check_password(plain_password, hashed_password):
    # Verify the password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)