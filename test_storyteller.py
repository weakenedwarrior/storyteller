from unittest import TestCase

from storyteller import StoryTeller, StoryTellerError

class test_storyteller(TestCase):
    
    def setUp(self):
        self.story = StoryTeller()
        
    def test_story_teller_raise_error_if_no_player_installed(self):
        self.assertRaises(StoryTellerError,self.story.play)
        
    def test_can_list_stories(self):
        self.assertIsInstance(self.story.listAll(),list)
        
    def test_can_set_a_story(self):
        self.story.add('FirstStory')
        self.assertTrue(len(self.story.listAll())==1)
        
    def test_can_set_the_story_player(self):
        self.story.setPlayer(MockPlayer)
        self.story.play()
        
        
class MockPlayer(object):
    
    @staticmethod
    def play():
        pass
        
    
        
        