from .Telegram_bot_server import remind_user_about_event
from .requests_client import requests_client_interface
from datetime import datetime
from . import small_redis_ORM
import time

def schedule_message_loop():
    while True:
        now = datetime.now()
        time_str = now.strftime("%H_%M")
        # TODO Исправить костыль
        keys_list = small_redis_ORM.get_shedule_messages_for_today(time_str)
        # print(keys_list)
        if len(keys_list)>0:
            for key in keys_list:
                _,user_event = key.split(':U:')
                user_id, event_id = user_event.split(':E:')
                small_redis_ORM.delete_shedule_messages(key)
                remind_user_about_event(user_id, event_id)
        time.sleep(5)

