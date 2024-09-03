import os
BOT_TOKEN=os.environ['BOT_TOKEN']
INVITE=os.environ['INVITE']
if not INVITE.endswith('/'):INVITE+='/'
PUNISH_ROLES=[x.strip() for x in os.environ['PUNISH_ROLES'].split(',')]
REDIS_URL=os.environ['REDIS_URL']
REDIS_USER=os.environ['REDIS_USER']
REDIS_PSW=os.environ['REDIS_PSW']