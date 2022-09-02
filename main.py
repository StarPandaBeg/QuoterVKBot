import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from handler import *
from config import *

def main():
    session = vk_api.VkApi(token=TOKEN)
    vk = session.get_api()
    longpoll = VkBotLongPoll(session, GROUP_ID)

    for event in longpoll.listen():
        if (event.type == VkBotEventType.MESSAGE_NEW):
            try:
                handle_message(event, vk)
            except:
                pass

if __name__ == "__main__":
    main()