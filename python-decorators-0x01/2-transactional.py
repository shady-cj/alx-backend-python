import sqlite3
import functools

"""your code goes here"""


def with_db_connection(func):
    """your code goes here"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        return func(conn, *args, **kwargs)

    return wrapper


def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = args[0]
        try:
            func(*args, **kwargs)
            conn.commit()
        except Exception as e:
            print("an error occured", str(e))
            conn.rollback()

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


#### Update user's email with automatic transaction handling

update_user_email(user_id=1, new_email="Crawford_Cartwright@hotmail.com")
