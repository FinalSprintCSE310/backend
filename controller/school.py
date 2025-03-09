from db.execute import GetCursor

def GetAllSchoolsController():
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