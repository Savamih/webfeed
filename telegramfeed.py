from time import sleep

import requests

TELEGRAM_TOKEN = "161996620:AAHlm4ShoPFCK8PP3xX14hAbVp8zR-Iuz-o/"
TELEGRAM_URL = "https://api.telegram.org/bot" + TELEGRAM_TOKEN


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(TELEGRAM_URL + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(get_updates_json(TELEGRAM_URL))['update_id']
    while True:
        if update_id == last_update(get_updates_json(TELEGRAM_URL))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(TELEGRAM_URL))), 'test')
            update_id += 1
        sleep(1)


if __name__ == '__main__':
    main()
