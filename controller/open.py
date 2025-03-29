# This controller is for the functions that returns the deatils that does not require any authentication prior
from db.execute import GetCursor
from helper.helper import GetColumnsJSON_Helper

def GetAllSchools_Controller():
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = '''SELECT "Id" AS "SchoolId", "Name" AS "SchoolName" FROM "public"."School"'''
    Cursor.execute(Query)
    Rows = Cursor.fetchall()
    Schools = GetColumnsJSON_Helper(Cursor, Rows)
    return Schools