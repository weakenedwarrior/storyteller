
class Monitor(object):

    def setSerial(self, SerialClass):
        self.ser = SerialClass()
        
    def setThreshold(self, threshold):
        self.threshold = threshold
        
    def getPosList(self):
        self.readline()
        return self.poslist 
    
    def getClosedSensors(self):
        self.readline()
        return [i for i in range(len(self.poslist)) if 0 < self.poslist[i] <= self.threshold]
    
    def getOpenSensors(self):
        self.readline()
        return [i for i in range(len(self.poslist)) if 0 == self.poslist[i] or self.threshold < self.poslist[i]]   
    
    def getTriggeredSensor(self):
        return self.getClosedSensors()[0]
    
    def sensorCount(self):
        try:
            return len(self.poslist)
        except AttributeError:
            raise SerialNotYetPolledError()    
    
    def readline(self):
        line = self.ser.readline()
        self.setPosList(line)
    
    def setPosList(self, line):
        self.poslist = []
        for elem in line.split(','):
            i, pos = elem.split(':')
            self.poslist.append(int(pos))
 
    def sensorCount(self):
        try:
            return len(self.poslist)
        except AttributeError:
            raise SerialNotYetPolledError()
    
    
class SerialNotYetPolledError(StandardError):
    pass