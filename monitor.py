
class Monitor(object):

    def __init__(self):
        self.currentSensor = None
        self.clearBuckets()

    def setSerial(self, SerialClass, device, baud):
        self.ser = SerialClass(device,baud)
        
    def setThreshold(self, threshold):
        self.threshold = threshold
        
    def getDistances(self):
        self.readline()
        return self.distances 
    
    def getClosedSensors(self):
        self.readline()
        return self.closedsensors
    
    def getOpenSensors(self):
        self.readline()
        return self.opensensors
    
    def getCurrentSensor(self):
        self.readline()
        return self.currentSensor
    
    def sensorCount(self):
        try:
            return len(self.distances)
        except AttributeError:
            raise SerialNotYetPolledError()    
    
    def readline(self):
        line = self.ser.readline()
        self.setDistances(line)
        self.bucketSensors()
        self.setCurrentSensor()
    
    def setDistances(self, line):
        self.distances = []
        line = line.strip(',')
        for pair in line.split(','):
            i, dist = pair.split(':')
            self.distances.append(int(dist))
        
    def bucketSensors(self):
        self.clearBuckets()
        for i, distance in enumerate(self.distances):
            self.putSensorInBucket(i, distance)        
        
    def setCurrentSensor(self):
        if self.closedsensors == []:
            self.currentSensor = None
        elif self.currentSensor not in self.closedsensors:
            self.currentSensor = self.closedsensors[0]
        
    def clearBuckets(self):
        self.opensensors = []
        self.closedsensors = []  
        
    def putSensorInBucket(self, i, dist):
        if self.isClosed(dist):
            self.closedsensors.append(i)
        else:
            self.opensensors.append(i) 
            
    def isClosed(self, distance):
        return 0 < distance <= self.threshold
    
    def getNextSensor(self):
        while(True):
            sensor = self.getCurrentSensor()
            if sensor:
                return sensor 
    
class SerialNotYetPolledError(StandardError):
    pass