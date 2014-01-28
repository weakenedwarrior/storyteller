from unittest import TestCase
import os

from player import Player, PlayerError, PLAYCMDS

TESTAUDIODIR = 'audio_test'

MISSINGSOUNDFILE = "NonExistentFile"
BADSOUNDFILE = "badsound.wav"
SOUNDTESTFILE = "digging.mp3"


class test_player(TestCase):
    
    def setUp(self):
        self.player = Player()
        self.player.setAudioDir(TESTAUDIODIR)
        self.player.setFile(SOUNDTESTFILE)
        
    def test_missing_file_raises_exception(self):
        self.assertRaises(PlayerError, self.player.setFile, MISSINGSOUNDFILE)
   
    def test_sound_file_includes_audioDir_path(self):
        self.assertEqual(self.player.getFile(), os.path.join(TESTAUDIODIR,SOUNDTESTFILE))
        
    def test_badsound_file_raises_exception(self):
        self.player.setFile(BADSOUNDFILE)
        self.assertRaises(PlayerError, self.player.play)    
        
    def test_unknown_os_raises_error(self):
        self.assertRaises(PlayerError, self.player.setCmdList, [(0,'UnknownOS','UnknownPlayer')])
        
    def test_playerCmd_set(self):
        self.assertIn(self.player.getPlayerCmd(), ['omxplayer','afplay'])
        
    def test_can_play_the_sound_file(self):
        self.player.play()
        
        
        
        