from .requests_client import requests_client_interface
import telebot
from telebot import types
from . import settings

telebot_token = settings.telebot_token
# aiohttp_call = aiohttp_client_interface.aiohttp_call

bot = telebot.TeleBot(telebot_token)

@bot.message_handler(commands=['ping'])
def ping_pong(message):
    result = requests_client_interface.ping()
    result = str(result)
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['start'])
def start(message):
    conf_id = str(message.chat.id)
    conf_options = '100'
    result = requests_client_interface.add_conf(conf_id=conf_id, conf_options=conf_options)['result']
    # print('result:',result)
    if result == 0:
        bot.send_message(message.chat.id, 'Бот уже работает в этой конференции')
    elif result == 1:
        bot.send_message(message.chat.id, '''Бот активирован.
Введите /help для получения информации,
/menu для управления ботом,
/event - тестовая команда''')


@bot.message_handler(commands=['help'])
def send_help(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, 'help', reply_markup=keyboard)


@bot.message_handler(commands=['menu'])
def send_menu(message):
    chat_id = str(message.chat.id)
    chat_exist = requests_client_interface.check_conf_exist(chat_id)['result']
    if chat_exist == 0:
        bot.send_message(message.chat.id, 'Для начала нужно активировать бота /start')
        return None
    
    bot_active_flag, event_cost_flag, filter_themes_flag = requests_client_interface.get_conf_options(chat_id)['conf_options']
    if bot_active_flag == '1':
        bot_active_text = '🟢 Бот включён'
    else:
        bot_active_text = '🔴 Бот выключен'
    
    if event_cost_flag == '1':
        event_cost_text = '🟤 Только бесплатные\n   мероприятия (пока недоступно)'
    else:
        event_cost_text = '🟤 Только бесплатные\n   мероприятия (пока недоступно)'

    if filter_themes_flag == '1':
        filter_themes_text = '🟢 Включена фильтрацию по темам'
    else:
        filter_themes_text = '🔴 Выключена фильтрация по темам'

    message_text = 'Меню бота:'+'\n'+bot_active_text+'\n'+event_cost_text+'\n'+filter_themes_text

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Вкл/выкл бота",callback_data='bot_active_button'))
    keyboard.add(types.InlineKeyboardButton(text="Вкл/выкл платные мероприятия",callback_data='event_cost_button'))
    keyboard.add(types.InlineKeyboardButton(text="Вкл/выкл фильтрацию по темам",callback_data='filter_themes_button'))
    if filter_themes_flag == '1':
        keyboard.add(types.InlineKeyboardButton(text="Настроить темы",callback_data='filter_themes_menu_button'))
    
    bot.send_message(message.chat.id, message_text, reply_markup=keyboard)


# def send_event_info(chat_id, event_id):
@bot.message_handler(commands=['event'])
def send_event_info(message):
    chat_id = message.chat.id
    # event_id = 'velopark'
    # event_id = '00000000'
    # event_id = '8892929292'
    event_id = '101011101'
    # keyboard = types.InlineKeyboardMarkup()
    # keyboard.add(types.InlineKeyboardButton(text="Вкл/выкл бота",callback_data='off_on_bot'))
    # keyboard.add(types.InlineKeyboardButton(text="Вкл/выкл платные мероприятия",callback_data='off_on_cost'))
    # keyboard.add(types.InlineKeyboardButton(text="Вкл/выкл подконференции",callback_data='off_on_subconfs'))
    # keyboard.add(types.InlineKeyboardButton(text="Настроить темы",callback_data='filter_theme'))
    # bot.send_message(message.chat.id, 'меню бота', reply_markup=keyboard)
    bot_active_flag, event_cost_flag, filter_themes_flag = requests_client_interface.get_conf_options(chat_id)['conf_options']
    if bot_active_flag == '0':
        bot.send_message(chat_id, 'бот выключен')
        return None

    if requests_client_interface.check_event_exist(event_id)['result'] == 0:
        bot.send_message(chat_id, 'event_id не существует')
        return None

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
    keyboard.add(types.InlineKeyboardButton(text="Перейти по ссылке",url=event_url))
    keyboard.add(types.InlineKeyboardButton(text="Я пойду",callback_data=f'user_go_event_button:{event_id}', pay='Строка'))
    keyboard.add(types.InlineKeyboardButton(text="Я не пойду",callback_data=f'user_doesnt_go_event_button:{event_id}'))
    keyboard.add(types.InlineKeyboardButton(text="Напомнить о мероприятии",callback_data=f'remind_user_go_event_button:{event_id}'))
    bot.send_message(chat_id, message_text, reply_markup=keyboard)




    # как отвечать на сообщение
	# bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     # keyboard = types.InlineKeyboardMarkup()
#     # url_button = types.InlineKeyboardButton(text="Перейти на Яндекс",callback_data='text')
#     # keyboard.add(url_button)
#     # bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    
#     # print(type(message))
#     # print(message)
#     if message.text.lower() == 'дай':
#         send_event_info(message.chat.id, 'velopark')
#     elif message.text.lower() == 'ping':
#         result = requests_client_interface.ping()
#         # result = str(result)
#         bot.send_message(message.chat.id, result)

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

# def send_event_info(chat_id, event_id):
#     if event_id in requests_client_interface.get_all_events():
#         event_name = requests_client_interface.get_event_name(event_id)['event_name']
#         event_descr = requests_client_interface.get_event_descr(event_id)['event_descr']
#         event_date = requests_client_interface.get_event_date(event_id)['event_date']
#         event_url = requests_client_interface.get_event_url(event_id)['event_url']
#         event_theme = requests_client_interface.get_event_theme(event_id)['event_theme']
#         message_text = f"""Мероприятие {event_name} ({event_date}).
# Описание: {event_descr}
# Ссылка: {event_url}
# Теги: {','.join(event_theme)}"""

#         keyboard = types.InlineKeyboardMarkup()
#         url_button = types.InlineKeyboardButton(text="Перейти по ссылке",url=event_url)
#         keyboard.add(url_button)
#         url_button = types.InlineKeyboardButton(text="Я пойду",callback_data='user_go_event')
#         keyboard.add(url_button)
#     else:
#         keyboard = types.InlineKeyboardMarkup()
#         message_text = f"Мероприятиe ({event_id}) не существует"
#     bot.send_message(chat_id, message_text, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'bot_active_button':
        result_dict = requests_client_interface.change_option_bot_active_for_conf(call.message.chat.id)
        if result_dict['result']:
            if result_dict['new_opt'] == '1':
                bot.send_message(call.message.chat.id, '🟢 Бот включён')
            else:
                bot.send_message(call.message.chat.id, '🔴 Бот выключен')
    elif call.data == 'event_cost_button':
        bot.answer_callback_query(callback_query_id=call.id, text='Данная функция ещё недопуступна.\nСкоро будет обновление.')
        # result_dict = requests_client_interface.change_option_event_cost_for_conf(call.message.chat.id)
        # if result_dict['result']:
        #     if result_dict['new_opt'] == '1':
        #         bot.send_message(call.message.chat.id, '🟤 Только бесплатные мероприятия')
        #     else:
        #         bot.send_message(call.message.chat.id, '🟤 Только бесплатные мероприятия')

    elif call.data == 'filter_themes_button':
        result_dict = requests_client_interface.change_option_filter_themes_for_conf(call.message.chat.id)
        if result_dict['result']:
            if result_dict['new_opt'] == '1':
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(types.InlineKeyboardButton(text="Настроить темы",callback_data='filter_themes_menu_button'))

                bot.send_message(call.message.chat.id, '🟢 Включена фильтрацию по темам', reply_markup=keyboard)
            else:
                bot.send_message(call.message.chat.id, '🔴 Выключена фильтрация по темам')

    elif call.data == 'filter_themes_menu_button':
        bot.send_message(call.message.chat.id, 'поменять темы')
    elif call.data.startswith('user_go_event_button:'):
        event_id = call.data.split(':')[1]
        user_id = call.from_user.id
        result = requests_client_interface.set_user_for_event(event_id, user_id)['result']
        if result == 1:
            bot.answer_callback_query(callback_query_id=call.id, text='Вы записаны на мероприятие.')
        elif result == 0:
            bot.answer_callback_query(callback_query_id=call.id, text='Вы уже записаны на мероприятие.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')

    elif call.data.startswith('user_doesnt_go_event_button:'):
        event_id = call.data.split(':')[1]
        user_id = call.from_user.id
        result = requests_client_interface.del_user_for_event(event_id, user_id)['result']
        if 1 in result:
            bot.answer_callback_query(callback_query_id=call.id, text='Запись и напоминание отменены.')
        elif result == [0,0]:
            bot.answer_callback_query(callback_query_id=call.id, text='Вы не были записаны на это мероприятие.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')

    elif call.data.startswith('remind_user_go_event_button:'):
        event_id = call.data.split(':')[1]
        user_id = call.from_user.id
        result = requests_client_interface.set_user_remind_for_event(event_id, user_id)['result']
        if result == 1:
            bot.answer_callback_query(callback_query_id=call.id, text='Поставлено напоминание для вас.')
        elif result == 0:
            bot.answer_callback_query(callback_query_id=call.id, text='Напоминание уже стоит.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')



bot.polling(none_stop=True, interval=0)


