from secrets import token_hex
from os import urandom
import hashlib as hash

def CreateSecretKey_Helper(Length = 128):
    try:
        SecretKey = token_hex(Length)
    except AttributeError:
        SecretKey = urandom(Length).hex()
    return SecretKey

def HashPassword_Helper(Password: str):
    return hash.sha256(Password.encode()).hexdigest()

def CheckPassword_Helper(Password, UserInput):
    if((Password == HashPassword_Helper(UserInput)) or (Password == UserInput)):
        return True
    else: 
        return False