from aura import *
from config import *
from flask import Flask, redirect

aura = Aura()
app = Flask(__name__)

@app.route('/')
def root():
    return "ok"

@app.route('/<id>')
def invite(id):
    user = aura.get(str(id))
    if user:
        user.balance+=120
        aura.update(user)
    return redirect(INVITE, code=302)

app.run('0.0.0.0', INVITE_SERVER_PORT)