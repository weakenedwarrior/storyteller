import os

class StoryTeller(object):
    
    def __init__(self):
        self.storylines = {}
        self.player = None
        self.audiodir = None
    
    def play(self):
        if self.player == None:
            raise NoPlayerSet
        self.player.play()            
    
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
        
        
class StoryTellerError(StandardError):
    pass

class NoPlayerSet(StoryTellerError):
    pass
