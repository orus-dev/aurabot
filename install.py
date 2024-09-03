from os import system as cmd, name

if name != 'nt':
    print('initializing environment')
    cmd('python3 -m venv .venv')
    print('installing discord.py')
    cmd('./.venv/bin/pip3 install discord.py')
    cmd('./.venv/bin/pip3 install Flask')
    # token = input('Bot Token>')
    # invite = input('Permanent Invite Link>')
    # with open('config.py', 'w') as f:
    #     f.write(f"BOT_TOKEN='{token}'\nINVITE='{invite}'")
    with open('aura.json', 'w') as f1:
        f1.write('{}')
else:
    print('installer currently does not support windows')