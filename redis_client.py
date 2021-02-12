import redis_ORM
# print(redis_ORM.set_event_id('myem',port=6379))
# event_info = {'event_id':12345, 'event_name':'танцы', 'event_descr':'супер-пупер',
#     'event_url':'http:nehttp', 'event_date':'2020-20-02', 'event_theme':'sport'}
# print(redis_ORM.get_all_events())
# print(redis_ORM.add_event(event_info=event_info))

redis_ORM.connection_to_redis()

