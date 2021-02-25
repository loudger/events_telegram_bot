from .Telegram_bot_server import *

def bot_polling_start():
    bot.polling(none_stop=True, interval=0)