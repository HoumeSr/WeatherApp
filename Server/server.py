import psycopg2
from decouple import config


class Server:
    def __init__(self):
        try:
            host = config("Host", cast=str)
            port = config("Port", cast=str)
            database = config("Database_Name", cast=str)
            username = config("Username", cast=str)
            password = config("Password", cast=str)
            self.conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)
        except Exception as Error:
            print("Can't establish connection to database")
            print(Error)


if __name__ == "__main__":
    server = Server()
