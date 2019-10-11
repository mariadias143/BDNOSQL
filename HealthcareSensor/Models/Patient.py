from datetime import date

class Patient:
    def __init__(self, patientid,name,birthdate,age,sensorid):
        self.patientid = patientid
        self.name = name
        self.birthdate = birthdate
        self.age = age
        self.sensorid = sensorid

    def getId(self):
        return self.patientid
    
    def getName(self):
        return self.name
    
    def getBirthDate(self):
        return self.birthdate
    
    def getAge(self):
        return self.age

    def getSensorId(self):
        return self.sensorid

    def insertQuery(self):
        return ("INSERT INTO Patient VALUES (%s,%s,%s,%s,%s)")

    def verifyQuery(self):
        return ("SELECT * FROM Patient WHERE patientid = %s")
    
    def data(self):
        return (self.patientid,self.name,self.birthdate,self.age,self.sensorid)
