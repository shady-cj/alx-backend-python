import time
import sqlite3
import functools

#### paste your with_db_decorator here

""" your code goes here"""


def with_db_connection(func):
    """your code goes here"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        return func(conn, *args, **kwargs)

    return wrapper


def retry_on_failure(retries, delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retry_count = retries
            while retry_count:
                try:
                    result = func(*args, **kwargs)
                    return result
                except:
                    time.sleep(delay)
                    retry_count -= 1
            return None

        return wrapper

    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=2)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userss")
    return cursor.fetchall()


#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
