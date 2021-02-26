import redis

# -------------------------------
# structure redis
# 
# events = (id1,id2.....idN)
# events:themes = (theme1.....themeK)
# event:<id>:name = str_name
# event:<id>:descr = ?
# event:<id>:url = str_url
# event:<id>:date = ?
# event:<id>:theme = (theme1, theme2, ... themeL)
# confs = (id1, id2....idM)
# conf:<id>:options = [0|1][0|1][0|1] // [activate bot][filter cost off/on][filter themes off/on]
# conf:<id>:themes = (theme1....themeJ)
# event:<id>:users = (id1, id2....idL)
# event:<id>:users_remind = (id1, id2....idX)
# 

# conf:<id>:event:<id>:subconf = str_url // Этот ключ удалён в силу невозможности реализации
# -------------------------------
# private methods

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 6379

def connection_to_redis(host=DEFAULT_HOST, port=DEFAULT_PORT):
    if host is None:
        host = DEFAULT_HOST
    if port is None:
        port = DEFAULT_PORT
    connection = redis.Redis(host=host , port=port, db=0, charset="utf-8", decode_responses=True)
    return connection

def decorator_connection(func):
    def wrapper(*args, **kwargs):
        if 'connection' not in kwargs:
            host = kwargs.get('host')
            port = kwargs.get('port')
            connection = connection_to_redis(host=host, port=port)
            kwargs['connection'] = connection
        return func(*args, **kwargs)
    return wrapper
    
# -------------------------------

def get_all_confs(**kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.smembers('confs')

def get_all_events(**kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.smembers('events')

def get_all_themes(**kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.smembers('events:themes')

def get_users_by_event(event_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.smembers(f'event:{event_id}:users')

def get_users_remind_by_event(event_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.smembers(f'event:{event_id}:users_remind')

def get_event_name(event_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.get(f'event:{event_id}:name')

def get_event_descr(event_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.get(f'event:{event_id}:descr')

def get_event_url(event_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.get(f'event:{event_id}:url')

def get_event_date(event_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.get(f'event:{event_id}:date')

def get_event_theme(event_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.smembers(f'event:{event_id}:theme')

# def get_subconf_by_conf_event(conf_id=None, event_id=None,**kwargs):
#     connection = connection_to_redis(**kwargs)
#     return connection.get(f'conf:{conf_id}:event:{event_id}:subconf')

def get_conf_options(conf_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.get(f'conf:{conf_id}:options')

def get_conf_themes(conf_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.smembers(f'conf:{conf_id}:themes')


def add_event(event_info=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    event_id = event_info['event_id']
    result = set_event_id(event_id, connection=connection)
    if result != 0:
        pipe = connection.pipeline()
        set_event_name(event_id, event_info['event_name'], connection=pipe)
        set_event_descr(event_id, event_info['event_descr'], connection=pipe)
        set_event_url(event_id, event_info['event_url'], connection=pipe)
        set_event_date(event_id, event_info['event_date'], connection=pipe)
        set_event_theme(event_id, event_info['event_theme'], connection=pipe)
        pipe.execute()
        # return pipe.execute()
        return 1
    return 0

@decorator_connection
def set_event_id(event_id=None, connection=None, **kwargs):
    if type(event_id) in [list, set, tuple]:
        return connection.sadd('events', *event_id)
    elif type(event_id) in [str, int]:
        return connection.sadd('events', event_id)

@decorator_connection
def set_event_name(event_id=None, event_name=None, connection=None, **kwargs):
    return connection.set(f'event:{event_id}:name', event_name)

@decorator_connection
def set_event_descr(event_id=None, event_descr=None, connection=None, **kwargs):
    return connection.set(f'event:{event_id}:descr', event_descr)

@decorator_connection
def set_event_url(event_id=None, event_url=None, connection=None, **kwargs):
    return connection.set(f'event:{event_id}:url', event_url)

@decorator_connection
def set_event_date(event_id=None, event_date=None, connection=None, **kwargs):
    return connection.set(f'event:{event_id}:date', event_date)

@decorator_connection
def set_event_theme(event_id=None, event_theme=None, connection=None, **kwargs):
    if type(event_theme) in [list, set, tuple]:
        return connection.sadd(f'event:{event_id}:theme', *event_theme)
    elif type(event_theme) in [str, int]:
        return connection.sadd(f'event:{event_id}:theme', event_theme)

def add_conf(conf_info=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    conf_id = conf_info['conf_id']
    result = set_conf_id(conf_id, connection=connection)
    if result != 0:
        pipe = connection.pipeline()
        if conf_info.get('conf_options') is not None:
            set_options_for_conf(conf_id, conf_info['conf_options'], connection=pipe)
        else:
            set_options_for_conf(conf_id, connection=pipe)
        if conf_info.get('conf_themes') is not None:
            set_themes_for_conf(conf_id, conf_info['conf_themes'], connection=pipe)
        pipe.execute()
        return 1
    return 0

@decorator_connection
def set_conf_id(conf_id=None, connection=None, **kwargs):
    if type(conf_id) in [list, set, tuple]:
        return connection.sadd('confs', *conf_id)
    elif type(conf_id) in [str, int]:
        return connection.sadd('confs', conf_id)
    else:
        return 0

@decorator_connection
def set_options_for_conf(conf_id=None, conf_options='000', connection=None, **kwargs):
    return connection.set(f'conf:{conf_id}:options', conf_options)

@decorator_connection
def set_themes_for_conf(conf_id=None, conf_themes=None, connection=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    if type(conf_themes) in [list, set, tuple]:
        return connection.sadd(f'conf:{conf_id}:themes', *conf_themes)
    elif type(conf_themes) in [str, int]:
        return connection.sadd(f'conf:{conf_id}:themes', conf_themes)

# def set_subconf_for_conf_event(conf_id=None, event_id=None, subconf_url=None, **kwargs):
#     connection = connection_to_redis(**kwargs)
#     return connection.set(f'conf:{conf_id}:event:{event_id}:subconf',subconf_url)

def set_user_for_event(event_id=None, user_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    if type(user_id) in [list, set, tuple]:
        return connection.sadd(f'event:{event_id}:users', *user_id)
    elif type(user_id) in [str, int]:
        return connection.sadd(f'event:{event_id}:users', user_id)

def set_user_remind_for_event(event_id=None, user_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    if type(user_id) in [list, set, tuple]:
        return connection.sadd(f'event:{event_id}:users_remind', *user_id)
    elif type(user_id) in [str, int]:
        return connection.sadd(f'event:{event_id}:users_remind', user_id)

def add_new_theme(theme = None, **kwargs):
    connection = connection_to_redis(**kwargs)
    if type(theme) in [list, set, tuple]:
        return connection.sadd(f'events:themes', *theme)
    elif type(theme) in [str, int]:
        return connection.sadd(f'events:themes', theme)


def del_conf(conf_id=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    keys_for_delete = connection.keys(f'conf:{conf_id}:*')
    pipe = connection.pipeline()
    pipe.srem(f'confs', conf_id)
    # pipe.delete(f'conf:{conf_id}:options')
    # pipe.delete(f'conf:{conf_id}:themes')
    # pipe.delete(f'conf:{conf_id}:*')
    for key_for_delete in keys_for_delete:
        pipe.delete(key_for_delete)
    return pipe.execute()

def del_event(event_id=None ,**kwargs):
    connection = connection_to_redis(**kwargs)
    pipe = connection.pipeline()
    pipe.srem(f'events', event_id)
    pipe.delete(f'event:{event_id}:name')
    pipe.delete(f'event:{event_id}:descr')
    pipe.delete(f'event:{event_id}:url')
    pipe.delete(f'event:{event_id}:date')
    pipe.delete(f'event:{event_id}:theme')
    pipe.delete(f'event:{event_id}:users')
    pipe.delete(f'event:{event_id}:users_remind')
    return pipe.execute()

def del_user_for_event(event_id=None ,user_id=None ,**kwargs):
    connection = connection_to_redis(**kwargs)
    pipe = connection.pipeline()
    if type(user_id) in [list, set, tuple]:
        pipe.srem(f'event:{event_id}:users_remind', *user_id)
        pipe.srem(f'event:{event_id}:users', *user_id)
    elif type(user_id) in [str, int]:
        pipe.srem(f'event:{event_id}:users_remind', user_id)
        pipe.srem(f'event:{event_id}:users', user_id)
    return pipe.execute()

def del_user_remind_for_event(event_id=None ,user_id=None ,**kwargs):
    connection = connection_to_redis(**kwargs)
    if type(user_id) in [list, set, tuple]:
        return connection.srem(f'event:{event_id}:users_remind', *user_id)
    elif type(user_id) in [str, int]:
        return connection.srem(f'event:{event_id}:users_remind', user_id)

def del_theme(theme = None,**kwargs):
    connection = connection_to_redis(**kwargs)
    return connection.srem(f'events:themes', theme)

def del_themes_for_conf(conf_id=None, conf_themes=None, **kwargs):
    connection = connection_to_redis(**kwargs)
    if type(conf_themes) in [list, set, tuple]:
        return connection.srem(f'conf:{conf_id}:themes', *conf_themes)
    elif type(conf_themes) in [str, int]:
        return connection.srem(f'conf:{conf_id}:themes', conf_themes)
