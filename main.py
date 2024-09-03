from config import *
from subprocess import run as run_start
from threading import Thread

env = os.environ.copy()

run = lambda a: run_start(a, env=env)

t1 = Thread(target=run, args=(['./.venv/bin/python3', 'invite_sys.py'],))
t2 = Thread(target=run, args=(['./.venv/bin/python3', 'bot.py'],))
t1.daemon = True
t2.daemon = True
if USE_INVITE_SERVER:t1.start()
t2.start()
while 1:
    if input() == 'q':
        if USE_INVITE_SERVER:t1.join(0)
        t2.join(0)