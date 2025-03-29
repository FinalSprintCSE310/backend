from db.execute import GetCursor
from helper.helper import CreateSecretKey_Helper, HashPassword_Helper
from datetime import date
from fastapi import Response


def AddNewUserAccount_Controller(Firstname: str, Lastname: str, Gender: str, DateOfBirth: date, Email: str, Password: str, Role: str, SchoolId: int):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = '''INSERT INTO "public"."User" ("Firstname", "Lastname", "Gender", "DateOfBirth", "Email", "Password", "Role", "SchoolId") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    Values = (Firstname, Lastname, Gender, DateOfBirth, Email, HashPassword_Helper(Password), Role, SchoolId)
    Cursor.execute(Query, Values)
    Cursor.connection.commit()
    Cursor.close()
    Cursor.connection.close()

def CheckIfUserExist_Controller(Search: str, Column: str):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Cursor.execute(f'''SELECT
    CASE
        WHEN "Name" IS NOT NULL THEN true
        ELSE false
    END AS user_status_description
FROM
    "School"
WHERE
    "{Column}" = '{Search}';''')
    Row = Cursor.fetchone()
    return Row

def UserLogin_Controller(Email: str, Password: str):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = '''SELECT "Id", "Role" FROM "public"."User" WHERE "Email" = %s AND "Password" = %s'''
    Values = (Email, HashPassword_Helper(Password))
    Cursor.execute(Query, Values)
    Row = Cursor.fetchone()
    return Row


def SetUserLoginCookie_Controller(UserId: int, UserRole: str, response: Response):
    Payload = {'UserId': UserId, 'IsAuthorized' : True, 'Role': UserRole}
    response.set_cookie(
        key="User_Session_Cookie",
        value=Payload,
        max_age=3600,
        httponly=True,
        secure=True,
        samesite="None"
    )