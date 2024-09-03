from subprocess import run
from threading import Thread

t1 = Thread(target=run, args=(['./.venv/bin/python3', 'invite_sys.py'],))
t2 = Thread(target=run, args=(['./.venv/bin/python3', 'main.py'],))
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
while 1:
    if input() == 'q':
        t1.join(0)
        t2.join(0)