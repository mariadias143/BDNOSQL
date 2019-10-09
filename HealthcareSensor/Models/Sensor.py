class Sensor:
    def __init__(self, sensorid,sensornum,typec):
        self.sensorid = sensorid
        self.sensornum = sensornum
        self.type = typec

    def insertQuery(self):
        return ("INSERT INTO Sensor VALUES (%s,%s,%s)")
    
    def data(self):
        return (self.sensorid,self.sensornum,self.type)