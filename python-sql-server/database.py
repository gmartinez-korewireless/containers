import pymssql, os, logging
from os import getenv

class Database(object):

    __connection = object

    def __init__(self):
        try:
            config = (getenv('DB_HOST'), getenv('DB_USER'), getenv('DB_PASS'), getenv('DB_NAME'))
            self.__connection = pymssql.connect(*config, as_dict=True)
        except Exception as error:
            logging.warning("Please make sure the connection varibles are setted.")
            logging.error(error)
            exit(1)
            pass
    
    def fetchall(self, sql, params=None):
        cursor = self.__execute(sql, params)
        return cursor.fetchone()
    
    def fetchone(self, sql, params=None):
        cursor = self.__execute(sql, params)
        return cursor.fetchone()

    def __execute(self, sql, params=None):
        cursor = self.__connection.cursor()
        cursor.execute(sql, params)
        return cursor

    def close(self):
        self.__connection.close()