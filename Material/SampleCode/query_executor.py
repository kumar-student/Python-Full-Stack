from sqlite3 import Error

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed")
    except Error as e:
        print(f"The error `{e}` occurred")