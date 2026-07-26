from pwdlib import PasswordHash

def hash_password(password : str):
    password = PasswordHash.recommended().hash(password)
    return password

def varify_password(plain_password, hash_password):
    password = PasswordHash.recommended().verify(plain_password, hash_password)
    return password