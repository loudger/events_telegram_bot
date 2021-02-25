import redis_ORM
# print(redis_ORM.set_event_id('myem',port=6379))
# event_info = {'event_id':12345, 'event_name':'танцы', 'event_descr':'супер-пупер',
#     'event_url':'http:nehttp', 'event_date':'2020-20-02', 'event_theme':'sport'}
# print(redis_ORM.get_all_events())
# print(redis_ORM.add_event(event_info=event_info))

# redis_ORM.connection_to_redis()

class admin_interface:
    @staticmethod
    def get_all_confs():
        result = redis_ORM.get_all_confs()
        return result

    @staticmethod
    def get_all_events():
        result = redis_ORM.get_all_events()
        return result

    @staticmethod
    def get_all_themes():
        result = redis_ORM.get_all_themes()
        return result

    @staticmethod
    def get_users_by_event(event_id):
        result = redis_ORM.get_users_by_event(event_id)
        return result

    @staticmethod
    def get_users_remind_by_event(event_id):
        result = redis_ORM.get_users_remind_by_event(event_id)
        return result

    @staticmethod
    def get_event_name(event_id):
        result = redis_ORM.get_event_name(event_id)
        return result

    @staticmethod
    def get_event_descr(event_id):
        result = redis_ORM.get_event_descr(event_id)
        return result

    @staticmethod
    def get_event_url(event_id):
        result = redis_ORM.get_event_url(event_id)
        return result

    @staticmethod
    def get_event_date(event_id):
        result = redis_ORM.get_event_date(event_id)
        return result

    @staticmethod
    def get_event_theme(event_id):
        result = redis_ORM.get_event_theme(event_id)
        return result

    @staticmethod
    def get_subconf_by_conf_event(conf_id, event_id):
        result = redis_ORM.get_subconf_by_conf_event(conf_id, event_id)
        return result

    @staticmethod
    def get_conf_options(conf_id):
        result = redis_ORM.get_conf_options(conf_id)
        return result

    @staticmethod
    def get_conf_themes(conf_id):
        result = redis_ORM.get_conf_themes(conf_id)
        return result


    @staticmethod
    def add_event(event_info):
        # event_info = {'event_id':..,'event_name':..,'event_descr':..,
        # 'event_url':..,'event_date':..,'event_theme':..}
        result = redis_ORM.add_event(event_info)
        return result

    @staticmethod
    def set_event_id(event_id):
        result = redis_ORM.set_event_id(event_id)
        return result

    @staticmethod
    def set_event_name(event_id, event_name):
        result = redis_ORM.set_event_name(event_id, event_name)
        return result

    @staticmethod
    def set_event_descr(event_id, event_descr):
        result = redis_ORM.set_event_descr(event_id, event_descr)
        return result

    @staticmethod
    def set_event_url(event_id, event_url):
        result = redis_ORM.set_event_url(event_id, event_url)
        return result

    @staticmethod
    def set_event_date(event_id, event_date):
        result = redis_ORM.set_event_date(event_id, event_date)
        return result

    @staticmethod
    def set_event_theme(event_id, event_theme):
        result = redis_ORM.set_event_theme(event_id, event_theme)
        return result

    @staticmethod
    def add_conf(conf_info):
        # conf_info = {'conf_id':..,'conf_options':..[,'conf_themes':..]}
        result = redis_ORM.add_conf(conf_info)
        return result

    @staticmethod
    def set_conf_id(conf_id):
        result = redis_ORM.set_conf_id(conf_id)
        return result

    @staticmethod
    def set_options_for_conf(conf_id, conf_options='000'):
        result = redis_ORM.set_options_for_conf(conf_id, conf_options)
        return result

    @staticmethod
    def set_themes_for_conf(conf_id, conf_themes):
        result = redis_ORM.set_themes_for_conf(conf_id, conf_themes)
        return result

    @staticmethod
    def set_subconf_for_conf_event(conf_id, event_id, subconf_url):
        result = redis_ORM.set_subconf_for_conf_event(conf_id, event_id, subconf_url)
        return result

    @staticmethod
    def set_user_for_event(event_id, user_id):
        result = redis_ORM.set_user_for_event(event_id, user_id)
        return result

    @staticmethod
    def set_user_remind_for_event(event_id, user_id):
        result = redis_ORM.set_user_remind_for_event(event_id, user_id)
        return result

    @staticmethod
    def add_new_theme(theme):
        result = redis_ORM.add_new_theme(theme)
        return result


    @staticmethod
    def del_conf(conf_id):
        result = redis_ORM.del_conf(conf_id)
        return result

    @staticmethod
    def del_event(event_id):
        result = redis_ORM.del_event(event_id)
        return result

    @staticmethod
    def del_user_for_event(event_id ,user_id):
        result = redis_ORM.del_user_for_event(event_id ,user_id)
        return result

    @staticmethod
    def del_user_remind_for_event(event_id ,user_id):
        result = redis_ORM.del_user_remind_for_event(event_id ,user_id)
        return result

    @staticmethod
    def del_theme(theme):
        result = redis_ORM.del_theme(theme)
        return result