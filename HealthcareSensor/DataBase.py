import mysql.connector

host = '127.0.0.1'
database = 'HealthcareSensors'

class DataBase:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def close(self):
        self.con.close()

    def open(self):
        self.con = mysql.connector.connect(user=self.user,
                                           password=self.password,
                                           host=host,
                                           database=database,
                                           )