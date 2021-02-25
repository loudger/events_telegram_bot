import requests
from . import settings

protocol = settings.protocol
default_host = settings.default_host
default_port = settings.default_port

class requests_client_interface:

    @classmethod
    def ping(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/ping')
        return result.text

    @classmethod
    def get_all_confs(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_all_confs')
        return result.json()

    @classmethod
    def get_all_events(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_all_events')
        return result.json()
    
    @classmethod
    def get_all_themes(cls):
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_all_themes')
        return result.json()

    @classmethod
    def get_users_by_event(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_users_by_event', params=params)
        return result.json()

    @classmethod
    def get_users_remind_by_event(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_users_remind_by_event', params=params)
        return result.json()

    @classmethod
    def get_event_name(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_name', params=params)
        return result.json()

    @classmethod
    def get_event_descr(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_descr', params=params)
        return result.json()

    @classmethod
    def get_event_url(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_url', params=params)
        return result.json()

    @classmethod
    def get_event_date(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_date', params=params)
        return result.json()

    @classmethod
    def get_event_theme(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_event_theme', params=params)
        return result.json()

    @classmethod
    def get_subconf_by_conf_event(cls, conf_id, event_id):
        params = {'conf_id':conf_id, 'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_subconf_by_conf_event', params=params)
        return result.json()

    @classmethod
    def get_conf_options(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_conf_options', params=params)
        return result.json()

    @classmethod
    def get_conf_themes(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/get_conf_themes', params=params)
        return result.json()

    @classmethod
    def add_conf(cls, conf_id, conf_options=None, conf_themes=None):
        params = {'conf_id':conf_id}
        if conf_options:
            params['conf_options'] = conf_options
        if conf_themes:
            params['conf_themes'] = conf_themes
        result = requests.post(f'{protocol}://{default_host}:{default_port}/add_conf', params=params)
        return result.json()

    @classmethod
    def set_options_for_conf(cls, conf_id, conf_options):
        params = {'conf_id':conf_id, 'conf_options':conf_options}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_options_for_conf', params=params)
        return result.json()

    @classmethod
    def set_themes_for_conf(cls, conf_id, conf_themes):
        params = {'conf_id':conf_id, 'conf_themes':conf_themes}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_themes_for_conf', params=params)
        return result.json()

    @classmethod
    def check_conf_exist(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/check_conf_exist', params=params)
        return result.json()

    @classmethod
    def check_event_exist(cls, event_id):
        params = {'event_id':event_id}
        result = requests.get(f'{protocol}://{default_host}:{default_port}/check_event_exist', params=params)
        return result.json()

    @classmethod
    def change_option_bot_active_for_conf(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/change_option_bot_active_for_conf', params=params)
        return result.json()

    @classmethod
    def change_option_event_cost_for_conf(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/change_option_event_cost_for_conf', params=params)
        return result.json()

    @classmethod
    def change_option_filter_themes_for_conf(cls, conf_id):
        params = {'conf_id':conf_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/change_option_filter_themes_for_conf', params=params)
        return result.json()




    # @classmethod
    # def set_subconf_for_conf_event(cls, conf_id, event_id, subconf_url):
    #     params = {'conf_id':conf_id, 'event_id':event_id, 'subconf_url':subconf_url}
    #     result = requests.post(f'{protocol}://{default_host}:{default_port}/set_subconf_for_conf_event', params=params)
    #     return result.json()

    @classmethod
    def set_user_for_event(cls, event_id, user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_user_for_event', params=params)
        return result.json()

    @classmethod
    def set_user_remind_for_event(cls, event_id, user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.post(f'{protocol}://{default_host}:{default_port}/set_user_remind_for_event', params=params)
        return result.json()

    @classmethod
    def del_user_for_event(cls, event_id ,user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.delete(f'{protocol}://{default_host}:{default_port}/del_user_for_event', params=params)
        return result.json()

    @classmethod
    def del_user_remind_for_event(cls, event_id ,user_id):
        params = {'event_id':event_id, 'user_id':user_id}
        result = requests.delete(f'{protocol}://{default_host}:{default_port}/del_user_remind_for_event', params=params)
        return result.json()





#     @classmethod
#     async def get_all_events(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_all_events", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_users_by_event(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_users_by_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_users_remind_by_event(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_users_remind_by_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_event_name(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_event_name", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_event_descr(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_event_descr", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_event_url(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_event_url", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_event_date(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_event_date", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_event_theme(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_event_theme", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_subconf_by_conf_event(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_subconf_by_conf_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_conf_options(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_conf_options", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def get_conf_themes(cls, session, *args, **kwargs):
#         async with session.get("{protocol}://{default_host}:8080/get_conf_themes", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def set_options_for_conf(cls, session, *args, **kwargs):
#         async with session.post("{protocol}://{default_host}:8080/set_options_for_conf", params=kwargs) as resp:
#             data = await resp.json()
#             return data
    
#     @classmethod
#     async def set_themes_for_conf(cls, session, *args, **kwargs):
#         async with session.post("{protocol}://{default_host}:8080/set_themes_for_conf", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def set_subconf_for_conf_event(cls, session, *args, **kwargs):
#         async with session.post("{protocol}://{default_host}:8080/set_subconf_for_conf_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def set_user_for_event(cls, session, *args, **kwargs):
#         async with session.post("{protocol}://{default_host}:8080/set_user_for_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def set_user_remind_for_event(cls, session, *args, **kwargs):
#         async with session.post("{protocol}://{default_host}:8080/set_user_remind_for_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def add_conf(cls, session, *args, **kwargs):
#         async with session.post("{protocol}://{default_host}:8080/add_conf", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def del_user_for_event(cls, session, *args, **kwargs):
#         async with session.delete("{protocol}://{default_host}:8080/del_user_for_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data

#     @classmethod
#     async def del_user_remind_for_event(cls, session, *args, **kwargs):
#         async with session.delete("{protocol}://{default_host}:8080/del_user_remind_for_event", params=kwargs) as resp:
#             data = await resp.json()
#             return data
# print(aio{protocol}_client_interface.aio{protocol}_call(aio{protocol}_client_interface.get_all_confs))

# print(requests_client_interface.get_all_confs())
# print(requests_client_interface.ping())