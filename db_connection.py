"""This file for database connection"""

import psycopg2

def database_connection():
    """This function for database connection"""
    connection = psycopg2.connect(
            dbname="Database Name", #Insert your database name
            user="User Name",#Insert your username
            password="Password",#Insert Your password
            host="Host Name",#Insert Your Host Name
            port="Port number"#Insert Your port number
    )
    curr = connection.cursor()
    return connection,curr

