from dbconnector import create_connection
from query_executor import execute_query

connection = create_connection("./sampledb.sqlite")

# users
#   id(integer)
#   name(text)
#   age(integer)
#   gender(text)
#   nationality(text)
create_user_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""
execute_query(connection, create_user_table)

# posts
# comments
# likes