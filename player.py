import os
import subprocess

PLAYCMDS = [(1,'raspberrypi','omxplayer'),
            (0,'Darwin','afplay')]

PROJECTDIR = '/home/pi/Projects/storyteller/'
DEFAULTAUDIODIR = PROJECTDIR + 'audio'

class Player(object):
        
    def __init__(self):
        self.soundFile = None
        self.setAudioDir(DEFAULTAUDIODIR)
        self.setCmdList(PLAYCMDS)
        
    def setCmdList(self, cmdlist):
        self.playerCmd = None
        self.setPlayerCmd(cmdlist)
        if self.playerCmd == None:
            raise PlayCmdNotSet        
    
    def setAudioDir(self,audioDir):
        self.audioDir = audioDir
    
    def isReady(self):
        return self.playerCmd != None and\
               self.soundFile != None
            
    def setPlayerCmd(self, cmdlist):
        for argpos,os_str,playcmd in cmdlist:
            if os.uname()[argpos] == os_str:
                self.playerCmd = playcmd
            
    def setFile(self,soundFile):
        self.soundFile = None
        soundFile = os.path.join(self.audioDir,soundFile)
        if os.path.isfile(soundFile):
            self.soundFile = soundFile
        else:
            raise MissingFile
            
    def getPlayerCmd(self):
        return self.playerCmd
    
    def getFile(self):
        return self.soundFile
    
    def play(self):
        if self.isReady():
            print 'Play audio from:', self.getFile()
            self.callSubProcess()
            
    def callSubProcess(self):
        try: 
            subprocess.check_call([self.playerCmd,self.soundFile]) 
        except subprocess.CalledProcessError:
            raise PlaySubProcessError
    
        
    
class PlayerError(StandardError):
    pass

class MissingFile(PlayerError):
    pass

class PlayCmdNotSet(PlayerError):
    pass

class PlaySubProcessError(PlayerError):
    pass
