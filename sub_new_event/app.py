import redis_ORM
from .requests_client_for_tg import requests_client_interface

def subscribe_to_new_event():
    connection = redis_ORM.connection_to_redis()
    connection_sub_event = connection.pubsub()
    connection_sub_event.subscribe('new_event')

    for new_event_id in connection_sub_event.listen():
        event_id = new_event_id['data']
        if event_id == 1:
            continue
        result_json = requests_client_interface.get_new_event_id(event_id)
        result = result_json['result']
        print(result)
