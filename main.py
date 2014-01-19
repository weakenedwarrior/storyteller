import serial
from storyteller import StoryTeller
from player import Player
from monitor import Monitor


AUDIODIR = 'audio'
THRESHOLD = 20
BAUD = 115200
DEVICE = '/dev/ttyUSB0'

if __name__ == '__main__':
    
    m = Monitor()
    m.setSerial(serial.Serial, DEVICE, BAUD)
    m.setThreshold(THRESHOLD)  
    m.flush()
    
    p = Player()
    
    s = StoryTeller()
    s.setPlayer(p)
    s.loadStoryLines()  
    
    while True:
        
        storyline = m.getNextSensor()
        
        print storyline
        
        #s.playNext(storyline)
    
    