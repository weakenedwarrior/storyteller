#!/usr/bin/python
import serial
from storyteller import StoryTeller
from player import Player
from monitor import Monitor

PROJECTDIR = '/home/pi/Projects/storyteller/'
AUDIODIR = PROJECTDIR + 'audio'
DEFAULT_THRESHOLD = 6  # in cm
SENSOR_THRESHOLDS = {4:3}  # in cm
BAUD = 115200
DEVICE = '/dev/ttyUSB0'

if __name__ == '__main__':
    
    print "Loading monitor..."
    m = Monitor()
    m.setSerial(serial.Serial, DEVICE, BAUD)
    m.setThresholds(DEFAULT_THRESHOLD, SENSOR_THRESHOLDS)  
    
    print "Loading stories..."
    s = StoryTeller()
    s.setAudioDir(AUDIODIR)
    s.setPlayer(Player)
    s.loadStoryLines() 
    print s.showStoryLines()
       
    s.playNext(10) # This is the startup message
       
    print "Starting main loop..."
    
    while True:
        
        print "Flushing ..."
        m.flush()
        storyline = m.getNextSensor()
        
        print "Closing serial"
        m.ser.close()
        
        print storyline
        s.playNext(storyline)
        
        print "Opening serial"
        m.ser.open()
        
        
    
    
