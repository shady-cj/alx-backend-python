from itertools import islice

stream_users = __import__("0-stream_users").stream_users


def stream_users_in_batches(batch_size):
    for user in islice(stream_users(), 0, batch_size):
        yield user


def batch_processing(batch_size):
    for user in stream_users_in_batches(batch_size):
        print(user)
