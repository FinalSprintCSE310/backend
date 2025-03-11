from db.execute import GetCursor

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

def CheckIfUserExist_Controller(Email: str):
    Cursor = GetCursor(True)
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
    "Email" = '{Email}';''')
    Row = Cursor.fetchone()
    print(Row)