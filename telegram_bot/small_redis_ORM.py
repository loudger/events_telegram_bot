import redis
from datetime import datetime


# -------------------------------
# structure redis
# 
# Единственный вид ключей это:
# D:{date}:T:{time}:U:{user_id}:E:{event_id}
# 

# -------------------------------
# private methods

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 6379
DEFAULT_DB = 1

def connection_to_redis(host=DEFAULT_HOST, port=DEFAULT_PORT, db = DEFAULT_DB):
    if host is None:
        host = DEFAULT_HOST
    if port is None:
        port = DEFAULT_PORT
    connection = redis.Redis(host=host , port=port, db=db, charset="utf-8", decode_responses=True)
    return connection

# -------------------------------


def set_shedule_message(user_id, event_id, date_time,**kwargs):
    connection = connection_to_redis(**kwargs)
    date, time = date_time.split(',')
    connection.set(f'D:{date}:T:{time}:U:{user_id}:E:{event_id}', 1)
    return 1

def get_shedule_messages_by_user_event(user_id, event_id ,**kwargs):
    connection = connection_to_redis(**kwargs)
    keys_list = connection.keys(f'*:U:{user_id}:E:{event_id}')
    return keys_list

def get_shedule_messages_for_today(time = None, **kwargs):
    connection = connection_to_redis(**kwargs)
    now = datetime.now()
    date = now.strftime("%d_%m_%Y")
    row_pattern = f'D:{date}:'
    if time is not None:
        row_pattern+= f'T:{time}:'
    row_pattern += '*'
    keys_list = connection.keys(row_pattern)
    return keys_list

def delete_shedule_messages_by_user_event(user_id, event_id,**kwargs):
    connection = connection_to_redis(**kwargs)
    keys_list = connection.keys(f'*:U:{user_id}:E:{event_id}')
    for key in keys_list:
        connection.delete(key)
    return 1

def delete_shedule_messages(key,**kwargs):
    connection = connection_to_redis(**kwargs)
    connection.delete(key)
    return 1