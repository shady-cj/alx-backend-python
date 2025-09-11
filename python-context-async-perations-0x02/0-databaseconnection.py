import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_conn = sqlite3.connect(db_name)

    def __enter__(self):
        cursor = self.db_conn.cursor()
        return cursor

    def __exit__(self, type, value, traceback):
        self.db_conn.close()


with DatabaseConnection("users.db") as cursor:
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
