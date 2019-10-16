import mysql.connector
from Models.Biometrics import Biometrics

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
        object.logs()

    def verify(self,object):
        self.open()

        cursor = self.con.cursor(buffered=True)
        cursor.execute(object.verifyQuery(),(object.getId(),))
        
        count = cursor.rowcount
        cursor.close()
        self.close()
        return count == 0

    def getBiometrics(self,userId):
        self.open()
        cursor = self.con.cursor(buffered=True)

        querie = ("Select B.bodytemp,B.systolic,B.diastolic,B.bpm,B.timestamp,B.sensorid FROM Biometrics as B, Patient as P , Sensor as S WHERE P.patientid = %s AND P.sensorid = S.sensorid AND B.sensorid = S.sensorid"
                )
        
        cursor.execute(querie,(userId,))

        bios = []

        for row in cursor:
            b = Biometrics(row[0],
                           row[1],
                           row[2],
                           row[3],
                           row[4],
                           row[5])
            bios.append(b)
        
        cursor.close()
        self.close()
        return bios
    
