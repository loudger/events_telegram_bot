from .requests_client import requests_client_interface
import telebot
from telebot import types
from . import settings

telebot_token = settings.telebot_token
# aiohttp_call = aiohttp_client_interface.aiohttp_call

bot = telebot.TeleBot(telebot_token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс",callback_data='text')
    keyboard.add(url_button)
    # bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    
    # print(type(message))
    # print(message)
    if message.text.lower() == 'дай':
        send_event_info(message.chat.id, 'velopark')
    elif message.text.lower() == 'ping':
        result = requests_client_interface.ping()
        # result = str(result)
        bot.send_message(message.chat.id, result)

    # print(type(message.from_user))
    # if message.text == "Привет":
    #     bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    # elif message.text == "/help":
    #     bot.send_message(message.from_user.id, "Напиши привет")
    # else:
    #     bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    # if message.text == "Привет":
    #     bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
    # elif message.text == "/help":
    #     bot.send_message(message.chat.id, "Напиши привет")
    # else:
    #     bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")

    

    # if message.text in ['/help','/help@besthangout_bot']:
    #     all_events = redis_ORM.get_all_events()
    #     bot.send_message(message.chat.id, \
    #             f'''Записаться на мероприятие:"/b пойду на id_мероприятия"\nДобавить мероприятие:"/b создать id_мероприятия"\nСписок кто записался:"/b кто записался на id_мероприятия"\nДоступные мероприятия {all_events}''', \
    #             reply_markup=keyboard)
    # elif message.text.startswith('/b'):
    #     if message.text.startswith('/b пойду на '):
    #         event_id = message.text.split()[-1]
    #         redis_ORM.set_user_for_event(event_id, message.from_user.id)
    #         bot.send_message(message.chat.id, f'Вы записались на "{event_id}"')
    #     elif message.text.startswith('/b создать '):
    #         event_id = message.text.split()[-1]
    #         redis_ORM.set_event_id(event_id)
    #         bot.send_message(message.chat.id, f'Добавлено мероприятие "{event_id}"')
    #     elif message.text.startswith('/b кто записался на '):
    #         event_id = message.text.split()[-1]
    #         users_id = redis_ORM.get_users_by_event(event_id)
    #         bot.send_message(message.chat.id, f'id пользователей, кто идёт на "{event_id}":{users_id}')
    #     else:
    #         bot.send_message(message.chat.id, f'Неверная команда. /help')

def send_event_info(chat_id, event_id):
    if event_id in requests_client_interface.get_all_events():
        event_name = requests_client_interface.get_event_name(event_id)['event_name']
        event_descr = requests_client_interface.get_event_descr(event_id)['event_descr']
        event_date = requests_client_interface.get_event_date(event_id)['event_date']
        event_url = requests_client_interface.get_event_url(event_id)['event_url']
        event_theme = requests_client_interface.get_event_theme(event_id)['event_theme']
        message_text = f"""Мероприятие {event_name} ({event_date}).
Описание: {event_descr}
Ссылка: {event_url}
Теги: {','.join(event_theme)}"""

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти по ссылке",url=event_url)
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Я пойду",callback_data='user_go_event')
        keyboard.add(url_button)
    else:
        keyboard = types.InlineKeyboardMarkup()
        message_text = f"Мероприятиe ({event_id}) не существует"
    bot.send_message(chat_id, message_text, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'user_go_event':
        bot.send_message(call.message.chat.id, f'Он идёт')
    # elif call.data == 'menu':
    #    print('"press button menu"')
    # print(call)



bot.polling(none_stop=True, interval=0)


