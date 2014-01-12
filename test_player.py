from unittest import TestCase

from player import Player, PlayerError

SOUNDTESTFILE = "testsound.wav"
BADSOUNDFILE = "NonExistentFile"


class test_player(TestCase):
    
    def test_instantiate_player_and_check_ifReady(self):
        player = Player()
        self.assertTrue(player.isReady())
        
    def test_can_play_the_sound_file(self):
        player = Player()
        player.play(SOUNDTESTFILE)
        
    def test_missing_file_raises_exception(self):
        player = Player()
        self.assertRaises(PlayerError, player.play, BADSOUNDFILE)
        