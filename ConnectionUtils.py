import Constants
import mysql.connector


def connection():
    try:
        c = mysql.connector.connect(
            host=Constants.host,
            user=Constants.username,
            passwd=Constants.password,
            database=Constants.database
        )
        return c
    except:
        print("Could not connect to database!")
        exit(1)