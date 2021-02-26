from .Telegram_bot_server import bot
from .routes import setup_routes
from . import settings
import threading
import aiohttp

host = settings.default_host_aiohttp_server
port = settings.default_port_aiohttp_server

def start_telebot():

    def aiohttp_server_app():
        app = aiohttp.web.Application()
        setup_routes(app)
        aiohttp.web.run_app(app, host = host, port = port)    

    def bot_polling_start():
        bot.polling(none_stop=True, interval=0)

    bot_threding = threading.Thread(target=bot_polling_start)
    bot_threding.start()

    aiohttp_server_app()



