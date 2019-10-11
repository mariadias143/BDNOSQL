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
                                           auth_plugin='mysql_native_password'
                                           )

    def insert(self,object):
        self.open()

        cursor = self.con.cursor()
        cursor.execute(object.insertQuery(),object.data())

        self.con.commit()
        cursor.close()
        self.close()

    def verify(self,object):
        self.open()

        cursor = self.con.cursor(buffered=True)
        cursor.execute(object.verifyQuery(),(object.getId(),))
        
        count = cursor.rowcount
        cursor.close()
        self.close()
        return count == 0