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
            self.setNextStory()
        else:
            raise PlayerNotReady

    def playNext(self, storyline):
        if storyline != self.currentstoryline:
            self.setCurrentStoryline(storyline)
        self.play()
        
    def playFirstOrRest(self, storyline):
        if storyline != self.currentstoryline:
            self.setCurrentStoryline(storyline)
            self.play() 
        else:
            self.playUntilFinished()
            
    def playUntilFinished(self):
        while not self.isFirstStory():
            self.play()
            
    def isFirstStory(self):
        return self.currentstoryindex == 0

    def setNextStory(self):
        self.currentstoryindex += 1
        self.currentstoryindex %= len(self.storylines[self.currentstoryline])
        self.setPlayerFile()

    def isReady(self):
        return self.player != None and self.currentstoryline in self.storylines
    
    def getStoryLines(self):
        return self.storylines
        
    def setPlayer(self, player):
        self.player = player()
        if self.audiodir:
            self.player.setAudioDir(self.audiodir)
        
    def setAudioDir(self, audiodir):
        self.audiodir = audiodir
        if self.player:
            self.player.setAudioDir(audiodir)
        
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
            self.storylines[index].sort()
        else:
            self.storylines[index] = [filename]
            
    def getIndex(self, filename):
        return int(filename.split('_',1)[0])
    
    def setCurrentStoryline(self, storyline):
        self.currentstoryline = storyline
        self.currentstoryindex = 0
        self.setPlayerFile()
        
    def getCurrentStory(self):
        return self.storylines[self.currentstoryline][self.currentstoryindex]
        
    def showStoryLines(self):
        allStories = []
        for story in self.storylines:
            allStories.extend(self.storylines[story])
        return '\n'.join(allStories)
    
    def setPlayerFile(self):
        self.player.setFile(self.getCurrentStory())        
        
class StoryTellerError(StandardError):
    pass

class PlayerNotReady(StoryTellerError):
    pass

