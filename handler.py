import json
from random import randint
from vk_api.bot_longpoll import VkBotMessageEvent
import loader

from config import *

if (USE_WHITELIST):
    with open('whitelist.json', 'r', encoding='utf-8') as f:
        WHITELIST = json.load(f)
else:
    WHITELIST = []

def handle_message(ev: VkBotMessageEvent, api):
    peer_id = int(ev.object.message['peer_id'])
    if peer_id not in WHITELIST and USE_WHITELIST:
        return

    text = get_text(ev)
    if not text.strip():
        return

    quote = ''
    try:
        if (text.isnumeric()):
            quote = loader.load_by_index(int(text))
        else:
            quote = loader.load_fuzzy(text)
    except:
        send_resp(ev, api, 'Цитата не найдена')
        return        

    send_resp(ev, api, quote)

def send_resp(ev: VkBotMessageEvent, api, msg):
    peer_id = ev.obj.message['peer_id']
    api.messages.send(peer_id = peer_id, message = msg, random_id = randint(0, 10000000))

def get_text(ev):
    raw = ev.obj.message['text']
    if raw.startswith('['):
        raw = raw[raw.find(']')+2:]
    return raw