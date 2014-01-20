import serial
from storyteller import StoryTeller
from player import Player
from monitor import Monitor


AUDIODIR = 'audio'
THRESHOLD = 4
BAUD = 115200
DEVICE = '/dev/ttyUSB0'

if __name__ == '__main__':
    
    print "Loading monitor..."
    m = Monitor()
    m.setSerial(serial.Serial, DEVICE, BAUD)
    m.setThreshold(THRESHOLD)  
    m.flush()
    
    print "Loading stories..."
    s = StoryTeller()
    s.setAudioDir(AUDIODIR)
    s.setPlayer(Player)
    s.loadStoryLines() 
    print s.showStoryLines()
       
    print "Starting main loop..."
    while True:
        
        storyline = m.getNextSensor()
        
        print storyline
        #s.playNext(storyline)
    
    
