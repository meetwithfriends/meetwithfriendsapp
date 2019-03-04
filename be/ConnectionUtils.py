import Constants
import mysql.connector

def connection():
    try:
        c = mysql.connector.connect(
            host=Constants.host,
            port=Constants.port,
            user=Constants.username,
            passwd=Constants.password,
            database=Constants.database
        )
        return c
    except mysql.connector.errors.Error as e:
        print("Connection failed:")
        print(e)
        