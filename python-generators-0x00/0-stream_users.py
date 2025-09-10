seed = __import__("seed")


def stream_users():
    """Generator function to stream user data from the database."""
    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data;")
        for row in cursor:
            yield row
        cursor.close()
