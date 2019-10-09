class Patient:
    def __init__(self, patientid,name,birthdate,age,sensorid):
        self.patientid = patientid
        self.name = name
        self.birthdate = birthdate
        self.age = age
        self.sensorid = sensorid

    def getPatientId(self):
        return self.patientid
    
    def getName(self):
        return self.name
    
    def getBirthDate(self):
        return self.birthdate
    
    def getAge(self):
        return self.age

    def getSensorId(self):
        return self.sensorid
