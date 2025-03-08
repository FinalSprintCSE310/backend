from dotenv import load_dotenv
import os
from connector import PostgresConnector


def Cursor():
    load_dotenv()
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    try:
        Cursor = PostgresConnector(USER, PASSWORD, HOST, PORT, DBNAME).GetCursor()
        return Cursor
    except:
        return False

def QueryResult(Cursor, Query, Flag, Parameters = False):
    try:
        Fetch = Cursor()
        try:
            match Flag:
                case 'Read':
                    print("Happy")
                    if not Parameters:
                        Fetch.execute(Query)
                    else:
                        Fetch.execute(Query, Parameters)
                    row = Fetch.fetchone()
                    return row
        except:
            return False
    except:
        return False