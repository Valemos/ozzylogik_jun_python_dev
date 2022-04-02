
from connection import *


def delete_by_first_digit():
    cursor = connection.cursor()
    cursor.execute("DELETE FROM random_strings WHERE LEFT(s1, 1) REGEXP '^[0-9]+$';")
    print(cursor.rowcount, "rows deleted")
    connection.commit()


if __name__ == '__main__':
    delete_by_first_digit()
