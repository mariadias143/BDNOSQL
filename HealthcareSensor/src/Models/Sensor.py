class Sensor:
    def __init__(self, sensorid,sensornum,typec):
        self.sensorid = sensorid
        self.sensornum = sensornum
        self.type = typec
    
    def getId(self):
        return self.sensorid

    def insertQuery(self):
        return ("INSERT INTO Sensor VALUES (%s,%s,%s)")

    def verifyQuery(self):
        return ("SELECT * FROM Sensor WHERE sensorid = %s")
    
    def data(self):
        return (self.sensorid,self.sensornum,self.type)
    
    def logs(self):
        print(f"Inseri o sensor com id {self.sensorid}")