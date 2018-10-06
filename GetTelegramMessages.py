# -*- coding: utf-8 -*-
import sys
import codecs
from telethon import TelegramClient, sync
import re

# These example values won't work. You must get your own api_id, phone_number and
# api_hash from https://my.telegram.org, under API Development.
api_id = 111111
api_hash = 'eXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
phone_number = '+YYXXXXXXXXX'

# Start the telegram client
client = TelegramClient('session_id', api_id, api_hash)

# Check if it is already authorized
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

# Get the chat_ids for the channels to do the search
hackplayers_id = client.get_entity('hackplayers').id
fwhibbit_id = client.get_entity('Fwhibbit').id
chat_ids = [hackplayers_id, fwhibbit_id]

# Define the search terms
search_terms = ['#ROJIRRINS', '#AZULONES', '#DULCINES', '#LECTURASENELROCA', '#ATMOSFERAPWN']

for search in search_terms:
    f= open(search.replace('#', '') + ".txt","w+")

    for chat in chat_ids:
        all_messages = client.get_messages(chat, None, search=search)
        for message in all_messages:
            f.write(str(message.message.replace('\n', ' ').encode('utf-8')))
            f.write('\n')

    f.close()
