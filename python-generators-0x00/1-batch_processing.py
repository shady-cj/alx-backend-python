from itertools import islice


seed = __import__("seed")


def stream_users_in_batches(batch_size):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data WHERE age > 25;")

    for user in islice(cursor.fetchall(), 0, batch_size):
        yield user


def batch_processing(batch_size):
    batch = []
    for user in stream_users_in_batches(batch_size):
        print(user)
        batch.append(user)
    return batch
