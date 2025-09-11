import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, parameter):
        self.db_conn = sqlite3.connect(db_name)
        self.query = query
        self.parameter = parameter

    def __enter__(self):
        cursor = self.db_conn.cursor()
        cursor.execute(self.query, self.parameter)
        return cursor.fetchall()

    def __exit__(self, type, value, traceback):
        self.db_conn.close()


with ExecuteQuery(
    "users.db", "SELECT * FROM users WHERE id = ? AND email = ?", (2, "bob@example.com")
) as results:
    for row in results:
        print(row)
