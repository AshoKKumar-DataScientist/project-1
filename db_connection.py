import mysql.connector
from mysql.connector import Error

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "ak1010"
DB_NAME = "cricketdb"


def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return conn

    except Error as e:
        print("Connection Error:", e)
        return None


if __name__ == "__main__":
    connection = get_connection()
    if connection:
        print("Database Connected Successfully")
        connection.close()
    else:
        print("Failed to connect")
