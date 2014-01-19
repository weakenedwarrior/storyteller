import serial
from storyteller import StoryTeller
from player import Player
from monitor import Monitor


AUDIODIR = 'audio'
THRESHOLD = 20
BAUD = 115200
DEVICE = '/dev/ttyACM0'

if __name__ == '__main__':
    
    ser = serial.Serial(DEVICE, BAUD)
    
    m = Monitor()
    m.setSerial(ser)
    m.setThreshold(THRESHOLD)    
    
    p = Player()
    
    s = StoryTeller()
    s.setPlayer(p)
    s.loadStoryLines()  
    
    while True:
        
        storyline = m.getNextSensor()
        s.playNext(storyline)
    
    