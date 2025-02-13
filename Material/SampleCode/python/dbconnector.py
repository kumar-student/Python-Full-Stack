import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connnection established")
    except Error as e:
        print(f"The error `{e}` occured")
    return connection