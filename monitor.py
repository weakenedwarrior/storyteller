
class Monitor(object):
    
    
    def setSerial(self, SerialClass):
        self.ser = SerialClass()
        
    def getPosList(self):
        line = self.ser.readline()
        self.setPosList(line)
        return self.poslist
    
    def setPosList(self, line):
        poslist = []
        for elem in line.split(','):
            i, pos = elem.split(':')
            poslist.append(int(pos))
        self.poslist = poslist
        

        