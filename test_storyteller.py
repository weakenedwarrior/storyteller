from unittest import TestCase
import os
import shutil

from storyteller import StoryTeller, StoryTellerError

AUDIODIR = 'audio'
TESTDIR = 'test'

AUDIOFILES = ['01_01_intro.wav',
              '01_02_content.wav',
              '02_01_intro.wav',
              '02_02_content.wav',
              '02_03_more_content.wav']

STORYLENGTHS = {1:2,
                2:3}

class test_storyteller(TestCase):
    
    def setUp(self):
        self.setUpStoryFiles()
        self.story = StoryTeller()
        self.story.setAudioDir(TESTDIR)
        self.story.loadStoryLines()
        
    def setUpStoryFiles(self):
        for filename in AUDIOFILES:
            self.touch(filename)
        
    def touch(self, filename):
        if not os.path.exists(TESTDIR):
            os.makedirs(TESTDIR) 
        fullname = os.path.join(TESTDIR,filename)
        with open(fullname, 'a'):
            os.utime(fullname, None)   
            
    def tearDown(self): 
        if os.path.exists(TESTDIR):
            shutil.rmtree(TESTDIR)
        
    def test_story_teller_raise_error_if_no_player_installed(self):
        self.assertRaises(StoryTellerError,self.story.play)
        
    def test_can_list_stories(self):
        storylines = self.story.getStoryLines()
        self.assertIsInstance(storylines,dict)
        count = len(STORYLENGTHS)
        self.assertEqual(len(storylines), count)
        for i in STORYLENGTHS:
            self.assertEqual(len(storylines[i]), STORYLENGTHS[i])
        
    def test_can_set_the_story_player(self):
        self.story.setPlayer(MockPlayer)
        self.story.play()
        
        
class MockPlayer(object):
    
    @staticmethod
    def play():
        pass
        
    
        
        