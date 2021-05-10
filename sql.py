import psycopg2
from cryptography.fernet import Fernet

class Sql:
    def __init__(self):  # конструктор, self = this, если используется нужно обьявлять, неявно не задано
        try:
            self.cnxn = psycopg2.connect(user="postgres",
                                         password="admin",
                                         host="localhost",
                                         port="5432",
                                         database="deanery",
                                         options="-c search_path=dbo,public")
            self.cursor = self.cnxn.cursor()

            print(self.cnxn.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
