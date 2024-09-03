from aura import *
from config import *
from flask import Flask, redirect
from os import environ

aura = Aura()
app = Flask(__name__)

@app.route('/<id>')
def root(id):
    user = aura.get(str(id))
    if user:
        user.balance+=120
        aura.update(user)
    return redirect(INVITE, code=302)

app.run('127.0.0.1', INVITE_SERVER_PORT)