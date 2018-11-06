import pymysql.cursors
import Constants


# Функция возвращает connection.
def getConnection():
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(host= Constants.host,
                                 user= Constants.username,
                                 password=Constants.password,
                                 db=Constants.db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection