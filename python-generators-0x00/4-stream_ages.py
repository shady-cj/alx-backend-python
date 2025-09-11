seed = __import__("seed")


def stream_user_ages():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data;")
    for row in cursor:
        yield row["age"]


def average_user_age():
    user_count = 0
    total_age = 0
    for age in stream_user_ages():
        total_age += age
        user_count += 1

    if user_count == 0:
        return

    avg = total_age / user_count
    print("Average age of users:", avg)
    return avg


if __name__ == "__main__":
    average_user_age()
