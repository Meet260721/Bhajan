"""This file for database connection"""

import psycopg2

def database_connection():
    """This function for database connection"""
    connection = psycopg2.connect(
            dbname="Demo",
            user="postgres",
            password="Meet@2712",
            host="localhost",
            port="5432"
    )
    curr = connection.cursor()
    return connection,curr

