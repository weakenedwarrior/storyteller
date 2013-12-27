import subprocess
import os

print os.uname()

subprocess.call(['afplay','one.m4a'])
subprocess.call(['afplay','two.m4a'])
subprocess.call(['afplay','three.m4a'])
