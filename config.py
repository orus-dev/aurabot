import os
print(os.environ)
BOT_TOKEN=os.environ['BOT_TOKEN']
USE_INVITE_SERVER=os.environ['USE_INVITE']=='true'
INVITE_SERVER_URL='127.0.0.1'
INVITE=os.environ['INVITE']
PUNISH_ROLES=(1279588925257683014,)