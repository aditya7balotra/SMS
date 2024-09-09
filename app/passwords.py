import bcrypt

def gen_hash(pswd):
    # generate a salt
    salt = bcrypt.gensalt()
    
    # hash the password using the salt
    hashed_pswd = bcrypt.hashpw(pswd.encode('utf-8'), salt)
    
    return hashed_pswd

