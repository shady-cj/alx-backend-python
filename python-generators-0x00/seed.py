import mysql.connector as mysql
from dotenv import load_dotenv
import os
import csv

load_dotenv()


def connect_db():
    try:
        db = mysql.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
        )
    except mysql.Error as err:
        print(f"Error: {err}")
        return None
    return db


def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except mysql.Error as err:
        print(f"Error", err)
        return None


def connect_to_prodev():
    try:
        db = mysql.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database="ALX_prodev",
        )
    except mysql.Error as err:
        print(f"Error", err)
        return None
    return db


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS user_data (
                    user_id CHAR(36) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    age DECIMAL(3, 0) NOT NULL
                )
            """
        )
    except mysql.Error as err:
        print(f"Error", err)
        return None


def insert_data(connection, data):
    try:
        with open(data, newline="") as file:
            reader = csv.DictReader(file)
            data = [(row["name"], row["email"], row["age"]) for row in reader]
        cursor = connection.cursor()
        cursor.executemany(
            "INSERT IGNORE INTO user_data(user_id, name, email, age) VALUES(UUID(), %s, %s, %s)",
            data,
        )
        connection.commit()
    except mysql.Error as err:
        print(f"Error", err)
        return None
