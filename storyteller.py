class StoryTeller(object):
    
    def __init__(self):
        self.storynames = []
        self.player = None
    
    def play(self):
        if self.player == None:
            raise NoPlayerSet
        self.player.play()            
    
    def listAll(self):
        return self.storynames
    
    def add(self,storyname):
        self.storynames.append(storyname)
        
    def setPlayer(self, player):
        self.player = player
        
class StoryTellerError(StandardError):
    pass

class NoPlayerSet(StoryTellerError):
    pass
