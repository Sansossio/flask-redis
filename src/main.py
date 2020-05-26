import os
from flask import Flask, request
from services import get_value, set_value

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/set')
def set():
  key = request.args.get('key')
  value = request.args.get('value')
  set_value(key, value)
  return 'OK'

@app.route('/get')
def get():
  key = request.args.get('key')
  return get_value(key)

if __name__ == '__main__':
    port = os.getenv('PORT') or 80
    app.run(
        host="0.0.0.0",
        port=port
    )
