import redis_ORM
from aiohttp import web
# import json

class client_interface:
    @staticmethod
    def ping(request: web.Request):
        return web.Response(text="pong")

    @staticmethod
    def get_all_confs(request: web.Request):
        result = redis_ORM.get_all_confs()
        result_json = list(result)
        return web.json_response(result_json)

    @staticmethod
    def get_all_events(request: web.Request):
        result = redis_ORM.get_all_events()
        result_json = list(result)
        return web.json_response(result_json)

    @staticmethod
    def get_all_themes(request: web.Request):
        result = redis_ORM.get_all_themes()
        result_json = list(result)
        return web.json_response(result_json)

    @staticmethod
    def get_users_by_event(request: web.Request):
        event_id = request.query['event_id']
        result = redis_ORM.get_users_by_event(event_id)
        result_json = list(result)
        return web.json_response(result_json)

    @staticmethod
    def get_users_remind_by_event(request: web.Request):
        event_id = request.query['event_id']
        result = redis_ORM.get_users_remind_by_event(event_id)
        result_json = list(result)
        return web.json_response(result_json)

    @staticmethod
    def get_event_name(request: web.Request):
        event_id = request.query.get('event_id',None)
        result = redis_ORM.get_event_name(event_id)
        result_json = {'event_name': result}
        return web.json_response(result_json)

    @staticmethod
    def get_event_descr(request: web.Request):
        event_id = request.query['event_id']
        result = redis_ORM.get_event_descr(event_id)
        result_json = {'event_descr': result}
        return web.json_response(result_json)

    @staticmethod
    def get_event_url(request: web.Request):
        event_id = request.query['event_id']
        result = redis_ORM.get_event_url(event_id)
        result_json = {'event_url': result}
        return web.json_response(result_json)

    @staticmethod
    def get_event_date(request: web.Request):
        event_id = request.query['event_id']
        result = redis_ORM.get_event_date(event_id)
        result_json = {'event_date': result}
        return web.json_response(result_json)

    @staticmethod
    def get_event_theme(request: web.Request):
        event_id = request.query['event_id']
        result = redis_ORM.get_event_theme(event_id)
        result_json = {'event_theme': list(result)}
        return web.json_response(result_json)

    @staticmethod
    def get_subconf_by_conf_event(request: web.Request):
        conf_id = request.query['conf_id']
        event_id = request.query['event_id']
        result = redis_ORM.get_subconf_by_conf_event(conf_id, event_id)
        result_json = {'sub_conf': result}
        return web.json_response(result_json)

    @staticmethod
    def get_conf_options(request: web.Request):
        conf_id = request.query['conf_id']
        result = redis_ORM.get_conf_options(conf_id)
        result_json = {'conf_options': result}
        return web.json_response(result_json)

    @staticmethod
    def get_conf_themes(request: web.Request):
        conf_id = request.query['conf_id']
        result = redis_ORM.get_conf_themes(conf_id)
        result_json = {'conf_themes': list(result)}
        return web.json_response(result_json)

    # def add_event(event_info):

    # def set_event_id(event_id):

    # def set_event_name(event_id, event_name):

    # def set_event_descr(event_id, event_descr):

    # def set_event_url(event_id, event_url):

    # def set_event_date(event_id, event_date):

    # def set_event_theme(event_id, event_theme):

    @staticmethod
    def add_conf(request: web.Request):
        conf_id = request.query['conf_id']
        conf_options = request.query.get('conf_options', '000')
        conf_themes = request.query.getall('conf_themes', None)
        conf_info = {'conf_id':conf_id, 'conf_options':conf_options}
        if conf_themes:
            conf_info['conf_themes'] = conf_themes
        result = redis_ORM.add_conf(conf_info)
        result_json = {'result': result}
        return web.json_response(result_json)

    # def set_conf_id(conf_id):

    @staticmethod
    def set_options_for_conf(request: web.Request):
        conf_id = request.query['conf_id']
        conf_options = request.query.get('conf_options', '000')
        result = redis_ORM.set_options_for_conf(conf_id, conf_options)
        result_json = {'result': str(result)}
        return web.json_response(result_json)

    @staticmethod
    def set_themes_for_conf(request: web.Request):
        conf_id = request.query['conf_id']
        conf_themes = request.query['conf_themes']
        result = redis_ORM.set_themes_for_conf(conf_id, conf_themes)
        result_json = {'result': str(result)}
        return web.json_response(result_json)

    @staticmethod
    def set_subconf_for_conf_event(request: web.Request):
        conf_id = request.query['conf_id']
        event_id = request.query['event_id']
        subconf_url = request.query['subconf_url']
        result = redis_ORM.set_subconf_for_conf_event(conf_id, event_id, subconf_url)
        result_json = {'result': str(result)}
        return web.json_response(result_json)

    @staticmethod
    def set_user_for_event(request: web.Request):
        event_id = request.query['event_id']
        user_id = request.query.getall('user_id')
        result = redis_ORM.set_user_for_event(event_id, user_id)
        result_json = {'result': result}
        return web.json_response(result_json)

    @staticmethod
    def set_user_remind_for_event(request: web.Request):
        event_id = request.query['event_id']
        user_id = request.query.getall('user_id')
        result = redis_ORM.set_user_remind_for_event(event_id, user_id)
        result_json = {'result': result}
        return web.json_response(result_json)

    @staticmethod
    def change_option_bot_active_for_conf(request: web.Request):
        change_opt = {'0':'1', '1':'0'}
        conf_id = request.query['conf_id']
        conf_options = redis_ORM.get_conf_options(conf_id=conf_id)
        new_opt = change_opt[conf_options[0]]
        conf_options= change_opt[conf_options[0]]+conf_options[1:]
        result = redis_ORM.set_options_for_conf(conf_id, conf_options)
        result_json = {'result': str(result), 'new_opt': new_opt}
        return web.json_response(result_json)

    @staticmethod
    def change_option_event_cost_for_conf(request: web.Request):
        change_opt = {'0':'1', '1':'0'}
        conf_id = request.query['conf_id']
        conf_options = redis_ORM.get_conf_options(conf_id=conf_id)
        new_opt = change_opt[conf_options[1]]
        conf_options = conf_options[0]+new_opt+conf_options[2]
        result = redis_ORM.set_options_for_conf(conf_id, conf_options)
        result_json = {'result': str(result), 'new_opt': new_opt}
        return web.json_response(result_json)

    @staticmethod
    def change_option_filter_themes_for_conf(request: web.Request):
        change_opt = {'0':'1', '1':'0'}
        conf_id = request.query['conf_id']
        conf_options = redis_ORM.get_conf_options(conf_id=conf_id)
        new_opt = change_opt[conf_options[2]]
        conf_options = conf_options[:2]+new_opt
        result = redis_ORM.set_options_for_conf(conf_id, conf_options)
        result_json = {'result': str(result), 'new_opt': new_opt}
        return web.json_response(result_json)

    @staticmethod
    def check_conf_exist(request: web.Request):
        conf_id = request.query['conf_id']
        result = redis_ORM.get_all_confs()
        if conf_id in result:
            result_json = {'result': 1}
        else:
            result_json = {'result': 0}
        return web.json_response(result_json)

    @staticmethod
    def check_event_exist(request: web.Request):
        event_id = request.query['event_id']
        result = redis_ORM.get_all_events()
        if event_id in result:
            result_json = {'result': 1}
        else:
            result_json = {'result': 0}
        return web.json_response(result_json)

    # def add_new_theme(request: web.Request, theme):

    # def del_conf(conf_id):

    # def del_event(event_id):

    @staticmethod
    def del_user_for_event(request: web.Request):
        event_id = request.query['event_id']
        user_id = request.query.getall('user_id')
        result = redis_ORM.del_user_for_event(event_id ,user_id)
        result_json = {'result': result}
        return web.json_response(result_json)

    @staticmethod
    def del_user_remind_for_event(request: web.Request):
        event_id = request.query['event_id']
        user_id = request.query.getall('user_id')
        result = redis_ORM.del_user_remind_for_event(event_id ,user_id)
        result_json = {'result': result}
        return web.json_response(result_json)

    # def del_theme(request: web.Request, theme):