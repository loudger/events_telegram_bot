from .requests_client import requests_client_interface
from .Telegram_bot_server import send_event_info
from .settings import X_API_Token
from aiohttp import web
import telebot


class API_methods:

    @staticmethod
    def get_new_event_id(request: web.Request):
        event_id = request.query['event_id']
        x_api_token_req = request.headers.get('authorization', None)
        if x_api_token_req == X_API_Token:
            print('coming new event')
            confs_ids = requests_client_interface.get_all_confs()
            for confs_id in confs_ids:
                try:
                    send_event_info(confs_id, event_id)
                except telebot.apihelper.ApiTelegramException:
                    pass
                except Exception as e:
                    print(e)
            print('event sended for all confs')
            result_json = {'result': 'OK'}
            return web.json_response(result_json)
        return web.HTTPBadRequest()
