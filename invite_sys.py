from aura import *
from config import *
from flask import Flask, redirect
from os import environ

aura = Aura('aura.json')
app = Flask(__name__)

@app.route('/<id>')
def root(id):
    aura.load()
    user = aura.get(str(id))
    if user:
        user.balance+=120
        aura.save()
    return redirect(INVITE, code=302)

app.run('127.0.0.1', INVITE_SERVER_PORT)