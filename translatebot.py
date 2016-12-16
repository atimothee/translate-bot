from flask import Flask
from flask import request, abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook')
def webhook():
    challenge = request.args.get('hub.challenge')
    token = request.args.get('hub.verify_token')
    if token == '54321':
        return challenge
    abort(500)


if __name__ == '__main__':
    app.run()
