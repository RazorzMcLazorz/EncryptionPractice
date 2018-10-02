import bcrypt

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode('utf8'), bcrypt.gensalt())

print(get_hashed_password('ourpassword'))

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf8'), hashed_password.encode('utf8'))

print(check_password('ourpassword', '$2b$12$T7P0TzaWAP5rGbg6Fkh49.ciLj89sxOTHiyZGysRb3esUWtNLtcHK'))
