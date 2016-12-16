__author__ = 'Timo'

import requests

JSON_HEADER = {'content': 'application/json'}


def post_message(sender, message, page_token):
    url = 'https://graph.facebook.com/v2.6/me/messages'
    params = {'access_token': page_token, 'recipient': {'id': sender}, 'message': message}
    return requests.post(url=url, json=params, headers=JSON_HEADER)


def build_image_message(image_url):
    m = {"attachment": {
        "type": "image",
        "payload": {
            "url": image_url
        }
    }}
    return m


def build_text_message(text):
    m = {"text": text}
    return m


def turn_typing_on(sender_id, access_token):
    url = "https://graph.facebook.com/v2.6/me/messages"
    data = {
        "recipient": {
            "id": sender_id
        },
        "access_token": access_token,
        "sender_action": "typing_on"
    }
    requests.post(url, json=data, headers=JSON_HEADER)


def turn_typing_off(sender_id, access_token):
    url = "https://graph.facebook.com/v2.6/me/messages"
    data = {
        "recipient": {
            "id": sender_id
        },
        "access_token": access_token,
        "sender_action": "typing_off"
    }
    requests.post(url, json=data, headers=JSON_HEADER)
