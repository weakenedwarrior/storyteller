class StoryTeller(object):
    
    def __init__(self):
        self.storynames = []
    
    def play(self):
        pass
    
    def listAll(self):
        return self.storynames
    
    def add(self,storyname):
        self.storynames.append(storyname)
        
        
