from flask import Flask
from flask import request, abort
from messenger_utils import build_text_message, post_message
import json

app = Flask(__name__)

page_token = "EAAX5N3qXfJwBAN2cqoKmez12T4VBF8ArtimSdJoMnrzWWb01oZAEFzRsNZASjRqGavTWBtBMnrRNYza6BZBwBfSin9J6INc0HYP2qteDbGB7yMaSX5ywf3gKwGBZCxfcD7pcIZCOieoT1EZAAK8rCbyDUu6wc8LjTuxELqRS2sOQZDZD"

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    j = request.json
    entries = j['entry']
    for e in entries:
        messages = e['messaging']
        for m in messages:
            sender_id = m['sender']['id']
            text = m['message']['text']
            post_message(sender_id, build_text_message(text), page_token)
    return 'replied'


if __name__ == '__main__':
    app.run()
