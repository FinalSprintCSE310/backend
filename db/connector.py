import psycopg2

class PostgresConnector:
    def __init__(self, User, Password, Host, Port, Database):
        self.User = User
        self.Password = Password
        self.Host = Host
        self.Port = Port
        self.Database = Database
    def GetConnection(self):
        try:
            Connection = psycopg2.connect(
                user=self.User,
                password=self.Password,
                host=self.Host,
                port=self.Port,
                dbname=self.Database
            )
            print("Connection successful!")
            # Create a cursor to execute SQL queries
            return Connection
        except:
            return False
