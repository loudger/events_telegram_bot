import requests
from . import settings


protocol = settings.protocol
default_host = settings.default_host
default_port = settings.default_port

header_token = {'authorization':settings.X_API_Token}

class requests_client_interface:

    @classmethod
    def ping(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/ping')

        return result.text

    @classmethod
    def get_all_confs(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_all_confs', headers=header_token)
        return result.json()

    @classmethod
    def get_all_events(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_all_events', headers=header_token)
        return result.json()
    
    @classmethod
    def get_all_themes(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_all_themes', headers=header_token)
        return result.json()

    @classmethod
    def get_users_by_event(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_users_by_event', params=params, headers=header_token)
        return result.json()

    @classmethod
    def get_users_remind_by_event(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_users_remind_by_event', params=params, headers=header_token)
        return result.json()

    @classmethod
    def get_event_name(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_name', params=params, headers=header_token)
        return result.json()

    @classmethod
    def get_event_descr(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_descr', params=params, headers=header_token)
        return result.json()

    @classmethod
    def get_event_url(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_url', params=params, headers=header_token)
        return result.json()

    @classmethod
    def get_event_date(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_date', params=params, headers=header_token)
        return result.json()

    @classmethod
    def get_event_theme(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_theme', params=params, headers=header_token)
        return result.json()

    # @classmethod
    # def get_subconf_by_conf_event(cls, conf_id, event_id):
    #     params = {'conf_id':conf_id, 'event_id':event_id}
    #     result = requests.get(f'{protocol}://{default_host}:{default_port}/get_subconf_by_conf_event', params=params, headers=header_token)
    #     return result.json()

    @classmethod
    def get_conf_options(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_conf_options', params=params, headers=header_token)
        return result.json()

    @classmethod
    def get_conf_themes(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_conf_themes', params=params, headers=header_token)
        return result.json()

    @classmethod
    def add_conf(cls, conf_id, conf_options=None, conf_themes=None):

        params = {'conf_id':conf_id}
        if conf_options:
            params['conf_options'] = conf_options
        if conf_themes:
            params['conf_themes'] = conf_themes
        result = requests.post(f'{protocol}://{default_host}:{default_port}/add_conf', params=params, headers=header_token)
        return result.json()

    @classmethod
    def set_options_for_conf(cls, conf_id, conf_options):
        params = {'conf_id':conf_id, 'conf_options':conf_options}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_options_for_conf', params=params, headers=header_token)
        return result.json()

    @classmethod
    def set_themes_for_conf(cls, conf_id, conf_themes):
        params = {'conf_id':conf_id, 'conf_themes':conf_themes}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_themes_for_conf', params=params, headers=header_token)
        return result.json()

    @classmethod
    def check_conf_exist(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/check_conf_exist', params=params, headers=header_token)
        return result.json()

    @classmethod
    def check_event_exist(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/check_event_exist', params=params, headers=header_token)
        return result.json()

    @classmethod
    def change_option_bot_active_for_conf(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/change_option_bot_active_for_conf', params=params, headers=header_token)
        return result.json()

    @classmethod
    def change_option_event_cost_for_conf(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/change_option_event_cost_for_conf', params=params, headers=header_token)
        return result.json()

    @classmethod
    def change_option_filter_themes_for_conf(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/change_option_filter_themes_for_conf', params=params, headers=header_token)
        return result.json()

    # @classmethod
    # def set_subconf_for_conf_event(cls, conf_id, event_id, subconf_url):
    #     params = {'conf_id':conf_id, 'event_id':event_id, 'subconf_url':subconf_url}
    #     result = requests.post(f'{protocol}://{default_host}:{default_port}/set_subconf_for_conf_event', params=params, headers=header_token)
    #     return result.json()

    @classmethod
    def set_user_for_event(cls, event_id, user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_user_for_event', params=params, headers=header_token)
        return result.json()

    @classmethod
    def set_user_remind_for_event(cls, event_id, user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_user_remind_for_event', params=params, headers=header_token)
        return result.json()

    @classmethod
    def del_user_for_event(cls, event_id ,user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.delete(f'{protocol}://{default_host}:{default_port}/del_user_for_event', params=params, headers=header_token)
        return result.json()

    @classmethod
    def del_user_remind_for_event(cls, event_id ,user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.delete(f'{protocol}://{default_host}:{default_port}/del_user_remind_for_event', params=params, headers=header_token)
        return result.json()

    @classmethod
    def del_themes_for_conf(cls, conf_id, conf_themes):
        params = {'conf_id':conf_id, 'conf_themes':conf_themes}
        result = requests.delete(f'{protocol}://{default_host}:{default_port}/del_themes_for_conf', params=params, headers=header_token)
        return result.json()


# print(requests_client_interface.set_options_for_conf('0101','101'))
# print(requests_client_interface.ping())