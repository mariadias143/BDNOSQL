class Biometrics:
    def __init__(self, bodytemp,systolic,diastolic,bpm,timestamp,sensorid):
        self.bodytemp = bodytemp
        self.systolic = systolic
        self.diastolic = diastolic
        self.bpm = bpm
        self.timestamp = timestamp
        self.sensorid = sensorid

    def getBodyTemp(self):
        return self.bodytemp
    
    def getSystolic(self):
        return self.systolic
    
    def getDiastolic(self):
        return self.diastolic
    
    def getBpm(self):
        return self.age

    def getTimeStamp(self):
        return self.timestamp

    def getSensorId(self):
        return self.sensorid
    
    def insertQuery(self):
        return ("INSERT INTO Biometrics (bodytemp,systolic,diastolic,bpm,timestamp,sensorid) VALUES (%s,%s,%s,%s,%s,%s)")
    
    def data(self):
        return (self.bodytemp,self.systolic,self.diastolic,self.bpm,self.timestamp,self.sensorid)