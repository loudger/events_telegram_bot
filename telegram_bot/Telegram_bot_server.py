import telebot
from telebot import types
from .requests_client import requests_client_interface
from . import settings
from . import small_redis_ORM

help_text = '''После добавления бота в конфу для начала его работы необходимо написать /start
Данный бот нацелен на нахождение различных мероприятий из интернет ресурсов и оповещение пользователей об этим мероприятиях.
Доступные команды:
/help - получение информации о пользованнии ботом;
/menu - меню бота, с помощью которого можно настроить бота, а также какие именно мероприятия вы хотите видеть.

Настройка бота в меню:
1. Можно выключить и включить бота.
2. Можно поставить фильтр только на бесплатные мероприятия (пока недоступно)
3. Можно настроить темы мероприятий

В случае включенной фильтрации по темам, Вам будут приходить уведомления мероприятий связанные с выбранными темами.
В случае выключенной фильтрации по темам, Вам будут приходить увидемления обо всех мероприятиях, найденные ботом. 

Когда приходит уведомление от бота по поводу мероприятия, Вы можете:
1. Нажать "Я пойду". В этом случае бот просто запишет вас в свою базу данных как участника.
2. Нажать "Напомнить о мероприятии". Бот напишет Вам, когда время мероприятия подойдёт к началу.
3. Нажать "Я не пойду". Бот удалит вас из своей базы данных как участника, а также не будет уведомлять Вас о начале мероприятия

Вы в любой момент можете передумать и выбрать любой из вариантов.
'''

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
    if result == 0:
        bot.send_message(message.chat.id, 'Бот уже работает в этой конференции')
    elif result == 1:
        bot.send_message(message.chat.id, '''Бот активирован.
Введите /help для получения информации,
/menu для управления ботом''')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, help_text)


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


def send_event_info(chat_id, event_id):
    bot_active_flag, event_cost_flag, filter_themes_flag = requests_client_interface.get_conf_options(chat_id)['conf_options']
    if bot_active_flag == '0':
        bot.send_message(chat_id, 'бот выключен')
        return None

    # print('bot activated')
    if requests_client_interface.check_event_exist(event_id)['result'] == 0:
        bot.send_message(chat_id, 'event_id не существует')
        return None

    # print('event exist')
    event_name = requests_client_interface.get_event_name(event_id)['event_name']
    event_descr = requests_client_interface.get_event_descr(event_id)['event_descr']
    event_date = requests_client_interface.get_event_date(event_id)['event_date']
    event_url = requests_client_interface.get_event_url(event_id)['event_url']
    event_theme = requests_client_interface.get_event_theme(event_id)

    if filter_themes_flag == '1':
        conf_themes = requests_client_interface.get_conf_themes(chat_id)
        theme_valid = True
        for conf_theme in conf_themes:
            if conf_theme in event_theme:
                theme_valid = False
        if theme_valid:
            return None

    # print('theme on')
    date_str, time_str = event_date.split(',')

    message_text = f"""Мероприятие {event_name}
Дата: {date_str.replace('_','.')} и время {time_str.replace('_',':')}.
Описание: {event_descr}
Ссылка: {event_url}
Теги: {','.join(event_theme)}"""

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Перейти по ссылке",url=event_url))
    keyboard.add(types.InlineKeyboardButton(text="Я пойду",callback_data=f'user_go_event_button:{event_id}', pay='Строка'))
    keyboard.add(types.InlineKeyboardButton(text="Я не пойду",callback_data=f'user_doesnt_go_event_button:{event_id}'))
    keyboard.add(types.InlineKeyboardButton(text="Напомнить о мероприятии",callback_data=f'remind_user_go_event_button:{event_id}'))
    bot.send_message(chat_id, message_text, reply_markup=keyboard)


def remind_user_about_event(user_id, event_id):
    # TODO переписать
    if requests_client_interface.check_event_exist(event_id)['result'] == 0:
        return None
    event_name = requests_client_interface.get_event_name(event_id)['event_name']
    event_url = requests_client_interface.get_event_url(event_id)['event_url']
    bot.send_message(user_id, f'Событие "{event_name}" начинается!\nСсылка: {event_url}')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # ------------------menu buttons------------------
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

    # --------------filter themes menu buttons--------------

    elif call.data == 'filter_themes_menu_button':
        all_themes_list = requests_client_interface.get_all_themes()
        conf_themes_list = requests_client_interface.get_conf_themes(call.message.chat.id)
        message_text_list = ['Меню тем:']
        print('conf_themes_list',conf_themes_list)
        for theme in all_themes_list:
            if theme in conf_themes_list:
                message_text_list.append(f'🟢 {theme}')
            else:
                message_text_list.append(f'🔴 {theme}')
        message_text = '\n'.join(message_text_list)
        
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Включить темы",callback_data='on_filter_themes_button'))
        keyboard.add(types.InlineKeyboardButton(text="Выключить темы",callback_data='off_filter_themes_button'))
        bot.send_message(call.message.chat.id, message_text, reply_markup=keyboard)

    # ------------add/remove theme for conf button------------

    elif call.data == 'on_filter_themes_button':
        all_themes_list = requests_client_interface.get_all_themes()
        conf_themes_list = requests_client_interface.get_conf_themes(call.message.chat.id)
        message_text = 'Включить темы:'
        

        keyboard_not_empty = False
        keyboard = types.InlineKeyboardMarkup()
        for theme in all_themes_list:
            if theme not in conf_themes_list:
                keyboard.add(types.InlineKeyboardButton(text=f"{theme}",callback_data=f'add_theme_for_conf_button:{theme}'))
                keyboard_not_empty = True

        if keyboard_not_empty:
            bot.send_message(call.message.chat.id, message_text, reply_markup=keyboard)
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Все темы уже выключены.')


    elif call.data == 'off_filter_themes_button':
        all_themes_list = requests_client_interface.get_all_themes()
        conf_themes_list = requests_client_interface.get_conf_themes(call.message.chat.id)
        message_text = 'Выключить темы:'

        keyboard_not_empty = False
        keyboard = types.InlineKeyboardMarkup()
        for theme in all_themes_list:
            if theme in conf_themes_list:
                keyboard.add(types.InlineKeyboardButton(text=f"{theme}",callback_data=f'delete_theme_for_conf_button:{theme}'))
                keyboard_not_empty = True

        if keyboard_not_empty:        
            bot.send_message(call.message.chat.id, message_text, reply_markup=keyboard)
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Все темы уже выключены.')


    elif call.data.startswith('add_theme_for_conf_button:'):
        theme = call.data.split(':')[1]

        result = requests_client_interface.set_themes_for_conf(call.message.chat.id, theme)['result']
        if result == "1":
            message_text = f'Тема {theme} теперь включена 🟢'
            bot.send_message(call.message.chat.id, message_text)
        elif result == "0":
            bot.answer_callback_query(callback_query_id=call.id, text='Тема уже включена.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')


    elif call.data.startswith('delete_theme_for_conf_button:'):
        theme = call.data.split(':')[1]

        result = requests_client_interface.del_themes_for_conf(call.message.chat.id, theme)['result']
        if result == "1":
            message_text = f'Тема {theme} теперь выключена 🔴'
            bot.send_message(call.message.chat.id, message_text)
        elif result == "0":
            bot.answer_callback_query(callback_query_id=call.id, text='Тема уже выключена.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')

    # --------------------event buttons--------------------

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
            if small_redis_ORM.delete_shedule_messages_by_user_event(user_id, event_id,) == 1:
                bot.answer_callback_query(callback_query_id=call.id, text='Запись и напоминание отменены.')
            else:
                bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')
        elif result == [0,0]:
            bot.answer_callback_query(callback_query_id=call.id, text='Вы не были записаны на это мероприятие.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')


    elif call.data.startswith('remind_user_go_event_button:'):
        event_id = call.data.split(':')[1]
        user_id = call.from_user.id
        result = requests_client_interface.set_user_remind_for_event(event_id, user_id)['result']
        if result == 1:
            date_time = requests_client_interface.get_event_date(event_id)['event_date']
            if small_redis_ORM.set_shedule_message(user_id, event_id, date_time) == 1:
                bot.answer_callback_query(callback_query_id=call.id, text='Поставлено напоминание для вас.')
            else:
                bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')
        elif result == 0:
            bot.answer_callback_query(callback_query_id=call.id, text='Напоминание уже стоит.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Просим прощение, в данным момент это невозможно.')
        



