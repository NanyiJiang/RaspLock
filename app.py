import lock
import os
import json

from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = json.load(open('.auth'))

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/lock', methods=['POST'])
@auth.login_required
def lock():
  lock.lock()

@app.route('/unlock', methods=['POST'])
@auth.login_required
def lock():
  lock.unlock()

@app.route('/')
@auth.login_required
def index():
  return "Hello, %s!" % auth.username()

if __name__ == '__main__':
  app.run('localhost', 5050)
