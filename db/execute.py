from dotenv import load_dotenv
import os
from db.connector import PostgresConnector
from psycopg2 import extras


def GetCursor(Mode=False): # This mode parameter is False for Dev Environment and True for Production
    load_dotenv()
    if Mode is False:
        USER = os.getenv("devuser")
        PASSWORD = os.getenv("devpassword")
        HOST = os.getenv("devhost")
        PORT = os.getenv("devport")
        DBNAME = os.getenv("devdbname")
    else:
        USER = os.getenv("user")
        PASSWORD = os.getenv("password")
        HOST = os.getenv("host")
        PORT = os.getenv("port")
        DBNAME = os.getenv("dbname")
    try:
        Connection = PostgresConnector(USER, PASSWORD, HOST, PORT, DBNAME).GetConnection()
        Cursor = Connection.cursor(cursor_factory=extras.DictCursor)
        return Cursor
    except:
        return False