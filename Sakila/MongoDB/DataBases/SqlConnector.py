import mysql.connector

host = '127.0.0.1'
database = 'sakila'

class SqlDataBase:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        self.open()

    def close(self):
        self.con.close()

    def open(self):
        self.con = mysql.connector.connect(user=self.user,
                                           password=self.password,
                                           host=host,
                                           database=database,
                                           auth_plugin='mysql_native_password'
                                           )

    def tablequery(self,querie):
        cursor = self.con.cursor(buffered=True)

        cursor.execute(querie)

        table = []

        for row in cursor:
            table.append(row)
        
        cursor.close()
        return table
    
    def queryWithArgs(self,querie,args):
        cursor = self.con.cursor(buffered=True)
        cursor.execute(querie,args)
        response = []

        for row in cursor:
            response.append(row)

        cursor.close()
        return response
    
    
    