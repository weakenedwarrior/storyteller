import os

class StoryTeller(object):
    
    def __init__(self):
        self.storylines = {}
        self.player = None
        self.audiodir = None
        self.currentstoryline = None
        self.currentstoryindex = 0
    
    def play(self):
        if self.isReady():
            self.player.play() 
            self.currentstoryindex += 1
            self.currentstoryindex %= len(self.storylines[self.currentstoryline])
        else:
            raise PlayerNotReady

    def playNext(self, storyline):
        if storyline != self.currentstoryline:
            self.setCurrentStoryline(storyline)
        self.play()

    def isReady(self):
        return self.player != None and self.currentstoryline in self.storylines
    
    def getStoryLines(self):
        return self.storylines
        
    def setPlayer(self, player):
        self.player = player
        
    def setAudioDir(self, audiodir):
        self.audiodir = audiodir
        
    def loadStoryLines(self):
        for filename in os.listdir(self.audiodir):
            if self.isValidAudioFile(filename):
                self.appendStory(filename)
        
    def isValidAudioFile(self, filename):
        return os.path.isfile(os.path.join(self.audiodir,filename))
    
    def appendStory(self,filename):
        index = self.getIndex(filename)
        if index in self.storylines:
            self.storylines[index].append(filename)
        else:
            self.storylines[index] = [filename]
            
    def getIndex(self, filename):
        return int(filename.split('_',1)[0])
    
    def setCurrentStoryline(self, storyline):
        self.currentstoryline = storyline
        self.currentstoryindex = 0
        
    def getCurrentStory(self):
        return self.storylines[self.currentstoryline][self.currentstoryindex]
        
        
class StoryTellerError(StandardError):
    pass

class PlayerNotReady(StoryTellerError):
    pass

