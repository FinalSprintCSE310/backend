from secrets import token_hex
from os import urandom
import hashlib as hash
from fastapi import Request

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
    
def GetColumnsJSON_Helper(Cursor, Rows):
    Columns = [desc[0] for desc in Cursor.description]
    JsonRows = [dict(zip(Columns, Row)) for Row in Rows]
    return JsonRows

def GetSchoolIdFromCookie(request):
    return eval(request.cookies.get("School_Session_Cookie", None))['SchoolId']