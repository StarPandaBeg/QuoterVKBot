import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from config import TOKEN, GROUP_ID
from func import get_logger
from handler import handle_message

def main():
    session = vk_api.VkApi(token=TOKEN)
    vk = session.get_api()
    longpoll = VkBotLongPoll(session, GROUP_ID)
    log = get_logger(__name__)

    log.info("Welcome to QuoterVKBot by StarPanda")
    
    while True:
        try:
            log.info("App started")
            event_loop(session, vk, longpoll)
        except KeyboardInterrupt:
            log.info("App stopped")
            break
        except Exception as e:
            log.warn("An error occured. Restarting server", e)

def event_loop(session, vk, longpoll):
    for event in longpoll.listen():
        if (event.type == VkBotEventType.MESSAGE_NEW):
            try:
                handle_message(event, vk)
            except:
                pass

if __name__ == '__main__':
    main()