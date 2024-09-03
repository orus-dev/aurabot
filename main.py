import os
env = os.environ.copy()
from config import *
from subprocess import run as run_start
from threading import Thread
import time

run = lambda a: run_start(a, env=env)
t1 = Thread(target=run, args=(['python3', 'invite_sys.py'],))
t2 = Thread(target=run, args=(['python3', 'bot.py'],))
t1.daemon = True
t2.daemon = True
if USE_INVITE_SERVER:t1.start()
t2.start()
while 1:
    time.sleep(.5)