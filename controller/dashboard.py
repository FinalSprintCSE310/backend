from db.execute import GetCursor
from helper.helper import GetColumnsJSON_Helper

def GetUsersForAuth_Controller(SchoolId: int):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = '''
SELECT "User"."Id", "User"."Firstname", "User"."Lastname", "User"."Role"
FROM "public"."School" AS "School"
INNER JOIN "public"."User" AS "User"
ON "School"."Id" = "User"."SchoolId"
WHERE "User"."IsAuthorized" IS FALSE AND "School"."Id" = %s;
'''
    Cursor.execute(Query, (SchoolId,))
    Rows = Cursor.fetchall()
    Users = GetColumnsJSON_Helper(Cursor, Rows)
    return Users

def AuthorizeUser_Controller(UserId: int, UserType: str):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = f'''
UPDATE "public"."User"
SET "IsAuthorized" = TRUE
WHERE "Id" = %s;
INSERT INTO "public"."{UserType}" ("UserId") VALUES (%s)
'''
    Cursor.execute(Query, (UserId, UserId,))
    Cursor.connection.commit()
    Cursor.close()
    Cursor.connection.close()

def GetAllParents_Controller(SchoolId: int):
    Cursor = GetCursor()
    if not Cursor:
        return False
    Query = '''
SELECT "User"."Firstname", "User"."Lastname", "User"."Role"
FROM "public"."School" AS "School"
INNER JOIN "public"."User" AS "User"
ON "School"."Id" = "User"."SchoolId"
INNER JOIN "public"."Parent" AS "Parent"
ON "User"."Id" = "Parent"."UserId"
WHERE "User"."SchoolId" = %s
'''
    Cursor.execute(Query, (SchoolId,))
    Rows = Cursor.fetchall()
    Parents = GetColumnsJSON_Helper(Cursor, Rows)
    return Parents