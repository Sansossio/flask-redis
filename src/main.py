import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Heroku!'

if __name__ == '__main__':
    port = os.getenv('PORT') or 80
    app.run(
        host="0.0.0.0",
        port=port
    )
