import lock
import os
import json

from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

auth_fn = os.path.join(os.path.dirname(__file__), '.auth')
users = json.load(open(auth_fn))

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/lock', methods=['POST'])
@auth.login_required
def f_lock():
  lock.lock()

@app.route('/unlock', methods=['POST'])
@auth.login_required
def f_unlock():
  lock.unlock()

@app.route('/')
@auth.login_required
def index():
  return "Hello, %s!" % auth.username()

if __name__ == '__main__':
  app.run('0.0.0.0', 5050)
