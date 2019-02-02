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
        exit(1)

    ''' except mysql.connector.errors.DatabaseError as e:
            try:
                c1 = mysql.connector.connect(
                    host=Constants.host,
                    port=Constants.port,
                    user=Constants.username,
                    passwd=Constants.password
                )
                print("Instance connection successful")
                print("Could not find meetwithfriends database!")
                print("Creating new database")
                script = open("scripts/init.sql", "r")
                s = script.read()
                c1.cursor().execute(s, True)
                c1.database = 'meetwithfriends'
                return c1
            except mysql.connector.errors.Error as e:
                if e == "Use multi=True when executing multiple statements":
                    return c1
                print("Err creating new database:")
                print(e)
                exit(1)'''