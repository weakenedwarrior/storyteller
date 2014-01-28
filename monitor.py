
class Monitor(object):

    def __init__(self):
        self.currentSensor = None
        self.clearBuckets()
        self.distances = None

    def setSerial(self, SerialClass, device, baud):
        self.ser = SerialClass(device,baud)
        
    def flush(self):
        self.ser.flushInput()
        self.previous_distances = None
        
    def setThresholds(self, default_threshold, sensor_thresholds):
        self.default_threshold = default_threshold
        self.sensor_thresholds = sensor_thresholds
        
    def getDistances(self):
        self.readline()
        return self.distances
    
    def getPreviousDistances(self):
        return self.previous_distances
    
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
        if self.distances == None:
            raise SerialNotYetPolledError() 
        else:
            return len(self.distances)
               
    def readline(self):
        line = self.getCleanLine()
        self.setDistances(line)
        self.bucketSensors()
        self.setCurrentSensor()
        
    def getCleanLine(self):
        line = ''
        while len(line) <= 5:  # All lines shorter are ignored
            line = self.ser.readline()
            line = line.strip()
        return line
    
    def setDistances(self, line):
        self.storeOldDistance()
        self.distances = []
        line = line.strip(',')
        for pair in line.split(','):
            i, dist = pair.split(':')
            self.distances.append(int(dist))
            
    def storeOldDistance(self):
        self.previous_distances = self.distances
        
    def bucketSensors(self):
        self.clearBuckets()
        for i, distance in enumerate(self.distances):
            if self.previous_distances == None or self.previous_distances[i] == 0:
                self.opensensors.append(i)
            else:
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
        if self.isClosed(i,dist):
            self.closedsensors.append(i)
        else:
            self.opensensors.append(i) 
            
    def isClosed(self,sensor,distance):
        if sensor in self.sensor_thresholds:
            threshold = self.sensor_thresholds[sensor]
        else:
            threshold = self.default_threshold       
        return 0 < distance <= threshold
    
    def getNextSensor(self):
        while(True):
            sensor = self.getCurrentSensor()
            if sensor != None:
                return sensor 
    
class SerialNotYetPolledError(StandardError):
    pass
