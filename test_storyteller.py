from unittest import TestCase

import storyteller

class test_storyteller(TestCase):
    
    def setUp(self):
        self.story = storyteller.StoryTeller()
        
    def test_story_teller_can_play_a_story(self):
        self.story.play()
        
    def test_can_list_stories(self):
        self.assertIsInstance(self.story.listAll(),list)
        
    def test_can_set_a_story(self):
        self.story.add('FirstStory')
        self.assertTrue(len(self.story.listAll())==1)
        
    
        
        