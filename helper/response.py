from secrets import token_hex
from os import urandom

def CreateSecretKey_Helper(Length = 128):
    try:
        SecretKey = token_hex(Length)
    except AttributeError:
        SecretKey = urandom(Length).hex()
    return SecretKey