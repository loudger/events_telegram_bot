import requests
from . import settings

protocol = settings.protocol
default_host = settings.default_host
default_port = settings.default_port

header_token = {'authorization':settings.X_API_Token}

class requests_client_interface:

    @classmethod
    def get_new_event_id(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_new_event_id', params=params, headers=header_token)
        return result.json()

