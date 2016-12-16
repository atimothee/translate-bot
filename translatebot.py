from flask import Flask
from flask import request, abort
from messenger_utils import build_text_message, post_message
import json
from google.cloud import translate

app = Flask(__name__)

page_token = "EAAX5N3qXfJwBAN2cqoKmez12T4VBF8ArtimSdJoMnrzWWb01oZAEFzRsNZASjRqGavTWBtBMnrRNYza6BZBwBfSin9J6INc0HYP2qteDbGB7yMaSX5ywf3gKwGBZCxfcD7pcIZCOieoT1EZAAK8rCbyDUu6wc8LjTuxELqRS2sOQZDZD"

translate_api_key = "AIzaSyAININRINK7bj8g2IhVgma6LSGHh-gblM0"

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
            try:
                post_message(sender_id, build_text_message(translate_text('fr', text)), page_token)
            except Exception, e:
                print e.message

    return 'replied'



def translate_text(target, text):
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

    return result['translatedText']


if __name__ == '__main__':
    app.run()
