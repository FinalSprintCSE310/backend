from db.connector import PostgresConnector
from db.execute import GetCursor
from helper.helper import CreateSecretKey_Helper, HashPassword_Helper
from fastapi import Response
from datetime import datetime, timedelta

def GetAllSchools_Controller():
    Cursor = GetCursor()
    if not Cursor:
        return False
    Cursor.execute("SELECT json_agg(json_build_object('name', name, 'abbrev', abbrev)) FROM pg_timezone_names;")
    Rows = Cursor.fetchall()
    print(Cursor.description)
    if not Rows:
        Cursor.close()
        return False
    return Rows[0][0]

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

def AddNewSchoolAccount_Controller(Name: str, Abbr: str, Zip: int, Email: str, Password: str):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = '''INSERT INTO "public"."School" ("Name", "Abbr", "Zip", "Email", "Password", "Route", "SecretKey" )VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    Values = (Name, Abbr, Zip, Email, HashPassword_Helper(Password), Abbr+'-'+str(Zip), CreateSecretKey_Helper())
    Cursor.execute(Query, Values)
    Cursor.connection.commit()
    Cursor.close()
    Cursor.connection.close()

def SchoolLogin_Controller(Email: str, Password: str):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = '''SELECT "Id" FROM "public"."School" WHERE "Email" = %s AND "Password" = %s'''
    Values = (Email, Password)
    Cursor.execute(Query, Values)
    Row = Cursor.fetchone()
    return Row

def SetSchoolLoginCookie_Controller(SchoolId: int, response: Response):
    Payload = {'SchoolId': SchoolId, 'IsAuthorized' : True}
    response.set_cookie(
        key="School_Session_Cookie",
        value=Payload,
        max_age=3600,
        httponly=True,
        secure=True,
        samesite="None"
    )