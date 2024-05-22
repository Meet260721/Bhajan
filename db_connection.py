"""This file for database connection"""

import psycopg2

class DatabaseConnector:
    def __init__(self,dbname,user,password,host,port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.cursor = None
        self.connection = None
    def database_connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password =self.password,
                host = self.host,
                port = self.port

            )
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully.")
        except psycopg2.Error as e:
            print("Unable to connect database.")

    def database_commit(self):
        if self.connection:
            self.connection.commit()
    def database_disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
