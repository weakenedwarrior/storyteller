import os

class Player(object):
    
    def isReady(self):
        return True
    
    def play(self, playfile):
        if not os.path.isfile(playfile):
            raise MissingFile
    
class PlayerError(StandardError):
    pass

class MissingFile(PlayerError):
    pass

