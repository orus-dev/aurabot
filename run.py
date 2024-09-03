from config import *
from subprocess import run
from threading import Thread

t1 = Thread(target=run, args=(['./.venv/bin/python3', 'invite_sys.py'],))
t2 = Thread(target=run, args=(['./.venv/bin/python3', 'main.py'],))
t1.daemon = True
t2.daemon = True
t1.start()
if USE_INVITE_SERVER:t2.start()
while 1:
    if input() == 'q':
        t1.join(0)
        if USE_INVITE_SERVER:t2.join(0)