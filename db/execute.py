from dotenv import load_dotenv
import os
from db.connector import PostgresConnector


def ConnectionString():
    load_dotenv()
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    try:
        Connection = PostgresConnector(USER, PASSWORD, HOST, PORT, DBNAME).GetConnection()
        return Connection
    except:
        return False

def QueryResult(Connection, Query, Flag, Parameters = False):
    try:
        Fetch = Connection.cursor()
        try:
            match Flag:
                case 'Read':
                    print("Read")
                    if not Parameters:
                        Fetch.execute(Query)
                    else:
                        Fetch.execute(Query, Parameters)
                    row = Fetch.fetchone()
                    return row
                case 'ReadAll':
                    print("Read All")
                    if not Parameters:
                        Fetch.execute(Query)
                    else:
                        Fetch.execute(Query, Parameters)
                    rows = Fetch.fetchall()
                    return rows
                case 'Other':
                    print('Insert Update Delete')
                    try:
                        Fetch.execute(Query, Parameters)
                        Connection.commit()
                    except:
                        Connection.rollback()
        except:
            return False
    except:
        return False