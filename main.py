#!/usr/bin/python
import serial
from storyteller import StoryTeller
from player import Player
from monitor import Monitor


AUDIODIR = 'audio'
THRESHOLD = 8  # Close senor threshold in cm
BAUD = 115200
DEVICE = '/dev/ttyUSB0'

if __name__ == '__main__':
    
    print "Loading monitor..."
    m = Monitor()
    m.setSerial(serial.Serial, DEVICE, BAUD)
    m.setThreshold(THRESHOLD)  
    
    print "Loading stories..."
    s = StoryTeller()
    s.setAudioDir(AUDIODIR)
    s.setPlayer(Player)
    s.loadStoryLines() 
    print s.showStoryLines()
       
    s.playNext(10) # This is the startup message
       
    print "Starting main loop..."
    
    while True:
        
        m.flush()
        storyline = m.getNextSensor()
        
        print storyline
        s.playNext(storyline)
        
        
    
    
