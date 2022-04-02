import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="tester",
    password="strong_password"
)


def init():
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_db;")
    connection.database = "test_db"

    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS random_strings ("
        "s0 VARCHAR(8),"
        "s1 VARCHAR(8),"
        "s2 VARCHAR(8),"
        "s3 VARCHAR(8),"
        "s4 VARCHAR(8),"
        "s5 VARCHAR(8)"
        ");"
    )


def drop():
    connection.database = "test_db"
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS random_strings;")


def get_all_rows():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM random_strings;")
    return cursor


def insert_line(line):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO random_strings (s0,s1,s2,s3,s4,s5) "
                   "VALUES (%s, %s, %s, %s, %s, %s);",
                   line)
    connection.commit()
