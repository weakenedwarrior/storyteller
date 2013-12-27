import subprocess
import os

audio_dir = 'audio'
os_data = os.uname()

if os_data[1] == 'rasberrypi':
    player = 'omxplayer'
elif os_data[0] == 'Darwin':
    player ='afplay'
else:
	raise StandardError('Unknown OS')

subprocess.call([player,os.path.join(audio_dir,'one.m4a')])
subprocess.call([player,os.path.join(audio_dir,'two.m4a')])
subprocess.call([player,os.path.join(audio_dir,'three.m4a')])
