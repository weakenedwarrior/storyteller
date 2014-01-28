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
        self.story.setPlayer(MockPlayer)
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
        
    def test_can_list_stories(self):
        storylines = self.story.getStoryLines()
        self.assertIsInstance(storylines,dict)
        count = len(STORYLENGTHS)
        self.assertEqual(len(storylines), count)
        for i in STORYLENGTHS:
            self.assertEqual(len(storylines[i]), STORYLENGTHS[i])
        
    def test_can_set_the_story_player(self):
        self.story.setCurrentStoryline(1)
        self.story.play()
        
    def test_if_current_storyline_not_set_raise_exception(self):
        self.assertRaises(StoryTellerError, self.story.play)
            
    def test_can_cycle_through_multiple_stories(self):
        self.story.setCurrentStoryline(1)
        self.assertCorrectFile(0)
        self.assertCorrectFile(1)
        self.assertCorrectFile(0)        
        self.story.setCurrentStoryline(2)
        self.assertCorrectFile(2)
        self.assertCorrectFile(3)
        self.assertCorrectFile(4)
        self.assertCorrectFile(2)
        
    def test_can_do_playNext(self):
        self.story.playNext(1)
        self.assertCorrectFile(1)
        self.story.playNext(2)
        self.story.playNext(2)
        self.story.playNext(2)
        self.assertCorrectFile(2)
        
        
    def test_can_do_playFirstOrRest(self):
        self.story.playFirstOrRest(1)
        self.story.playFirstOrRest(1)
        self.assertCorrectFile(0)
        self.story.playFirstOrRest(2)
        self.assertCorrectFile(3)
        self.story.playFirstOrRest(2)
        self.assertCorrectFile(2)
        
    def test_can_show_storylines(self):
        self.assertEqual(self.story.showStoryLines(), '\n'.join(AUDIOFILES))
           
    def assertCorrectFile(self, audiofileindex):
        self.assertEquals(self.story.getCurrentStory(),AUDIOFILES[audiofileindex])
        self.story.play()
     
        
class MockPlayer(object):
    
    def __init__(self):
        self.filename = None
        self.audiodir = None
    
    def setAudioDir(self, audiodir):
        self.audiodir = audiodir
    
    def play(self):
        if self.filename == None or self.audiodir == None:
            raise MockPlayerError
        
    def setFile(self, filename):
        self.filename = filename
        
class MockPlayerError(StandardError):
    pass
        
        

        
        