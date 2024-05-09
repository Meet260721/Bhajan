"""This file for database connection"""

import psycopg2

def database_connection():
    """This function for database connection"""
    connection = psycopg2.connect(
        dbname="DatabaseName",  # Insertyourdatabasename
        user="UserName",  # Insertyourusername
        password="Password",  # InsertYourpassword
        host="HostName",  # InsertYourHostName
        port="Portnumber"  # InsertYourportnumber

    )
    curr = connection.cursor()
    return connection,curr

