from .admin_API import admin_interface
import pytest

event_info = {'event_id':'test_id','event_name':'test_name','event_descr':'test_descr',
'event_url':'test_url','event_date':'test_date','event_theme':'test_them1'}
event_info2 = {'event_id':'test_id2','event_name':'test_name2','event_descr':'test_descr2',
'event_url':'test_url2','event_date':'test_date2','event_theme':['test_them1', 'test_them2']}

error_event_info = {'event_id':'test_id2','event_name':'test_name','event_descr':'test_descr',
'event_url':'test_url','event_date':'test_date','event_theme':['test_them1', 'test_them2']}

conf_info = {'conf_id':'test_id','conf_options':'000'}
conf_info2 = {'conf_id':'test_i2','conf_options':'010', 'conf_themes':'test_theme1'}
conf_info3 = {'conf_id':'test_id3','conf_options':'101', 'conf_themes':['test_theme1', 'test_theme1']}

# subconf_url = 'test_url'
# subconf_url2 = 'test_url2'

user_id = 'test_user_id'
user_id2 = ['test_user_id', 'test_user_id2']

def test_cleare_db_start():
    admin_interface.del_conf('test_id')
    admin_interface.del_event(event_info['event_id'])
    admin_interface.del_event(event_info2['event_id'])
    admin_interface.del_theme('test_theme')
    admin_interface.del_theme('test_theme2')
    all_confs = admin_interface.get_all_confs()
    all_events = admin_interface.get_all_events()
    all_themes = admin_interface.get_all_themes()
    expression = 'test_id' in all_confs or event_info['event_id'] in all_events or 'test_theme' in all_themes
    assert expression == False

def test_success_add_event():
    result = admin_interface.add_event(event_info)
    all_events = admin_interface.get_all_events()
    event_name = admin_interface.get_event_name('test_id')
    event_descr = admin_interface.get_event_descr('test_id')
    event_url = admin_interface.get_event_url('test_id')
    event_date = admin_interface.get_event_date('test_id')
    event_theme = admin_interface.get_event_theme('test_id')
    expression = result == 1 and event_info['event_id'] in all_events and\
        event_info['event_name'] == event_name and\
        event_info['event_descr'] == event_descr and\
        event_info['event_url'] == event_url and\
        event_info['event_date'] == event_date and\
        event_info['event_theme'] in event_theme
    assert expression == True

def test_error_add_event():
    result = admin_interface.add_event(event_info)
    all_events = admin_interface.get_all_events()
    assert result == 0 and event_info['event_id'] in all_events

def test_set_event_id():
    result = admin_interface.set_event_id(event_info2['event_id'])
    all_events = admin_interface.get_all_events()
    assert result == 1 and event_info2['event_id'] in all_events

def test_reset_event_id():
    result = admin_interface.set_event_id(event_info2['event_id'])
    all_events = admin_interface.get_all_events()
    assert result == 0 and event_info2['event_id'] in all_events

def test_set_event_name():
    result = admin_interface.set_event_name(event_info2['event_id'], event_info2['event_name'])
    event_name = admin_interface.get_event_name(event_info2['event_id'])
    assert result == 1 and event_info2['event_name'] == event_name

def test_set_event_descr():
    result = admin_interface.set_event_descr(event_info2['event_id'], event_info2['event_descr'])
    event_descr = admin_interface.get_event_descr(event_info2['event_id'])
    assert result == 1 and event_info2['event_descr'] == event_descr

def test_set_event_url():
    result = admin_interface.set_event_url(event_info2['event_id'], event_info2['event_url'])
    event_url = admin_interface.get_event_url(event_info2['event_id'])
    assert result == 1 and event_info2['event_url'] == event_url

def test_set_event_date():
    result = admin_interface.set_event_date(event_info2['event_id'], event_info2['event_date'])
    event_date = admin_interface.get_event_date(event_info2['event_id'])
    assert result == 1 and event_info2['event_date'] == event_date

def test_set_event_theme():
    result = admin_interface.set_event_theme(event_info2['event_id'], event_info2['event_theme'])
    event_theme = admin_interface.get_event_theme(event_info2['event_id'])
    expression = result == len(event_info2['event_theme'])
    for theme in event_info2['event_theme']:
        expression = expression and theme in event_theme
    assert expression

def test_reset_event_theme():
    result = admin_interface.set_event_theme(event_info['event_id'], event_info['event_theme'])
    assert result == 0


def test_success_add_conf():
    result = admin_interface.add_conf(conf_info)
    all_confs = admin_interface.get_all_confs()
    conf_options = admin_interface.get_conf_options(conf_info['conf_id'])
    assert result == 1 and conf_info['conf_id'] in all_confs and\
        conf_info['conf_options'] == conf_options

def test_error_add_conf():
    result = admin_interface.add_conf(conf_info)
    all_confs = admin_interface.get_all_confs()
    assert result == 0 and conf_info['conf_id'] in all_confs

def test_set_conf_id():
    result = admin_interface.set_conf_id(conf_info2['conf_id'])
    all_confs = admin_interface.get_all_confs()
    assert result == 1 and conf_info2['conf_id'] in all_confs

def test_reset_conf_id():
    result = admin_interface.set_conf_id(conf_info2['conf_id'])
    all_confs = admin_interface.get_all_confs()
    assert result == 0 and conf_info2['conf_id'] in all_confs

def test_set_options_for_conf():
    result = admin_interface.set_options_for_conf(conf_info2['conf_id'], conf_info2['conf_options'])
    conf_options = admin_interface.get_conf_options(conf_info2['conf_id'])
    assert result == True and conf_info2['conf_options'] == conf_options

def test_set_themes_for_conf():
    result = admin_interface.set_themes_for_conf(conf_info2['conf_id'], conf_info2['conf_themes'])
    conf_themes = admin_interface.get_conf_themes(conf_info2['conf_id'])
    assert result == 1 and conf_info2['conf_themes'] in conf_themes

def test_reset_themes_for_conf():
    result = admin_interface.set_themes_for_conf(conf_info2['conf_id'], conf_info2['conf_themes'])
    conf_themes = admin_interface.get_conf_themes(conf_info2['conf_id'])
    assert result == 0 and conf_info2['conf_themes'] in conf_themes

# def test_set_subconf_for_conf_event():
#     result = admin_interface.set_subconf_for_conf_event(conf_info['conf_id'], event_info['event_id'], subconf_url)
#     sc_url = admin_interface.get_subconf_by_conf_event(conf_info['conf_id'], event_info['event_id'])
#     assert result == 1 and subconf_url == sc_url

def test_set_user_for_event():
    result = admin_interface.set_user_for_event(event_info['event_id'], user_id)
    u_ids = admin_interface.get_users_by_event(event_info['event_id'])
    assert result == 1 and user_id in u_ids

def test_reset_user_for_event():
    result = admin_interface.set_user_for_event(event_info['event_id'], user_id)
    u_ids = admin_interface.get_users_by_event(event_info['event_id'])
    assert result == 0 and user_id in u_ids

def test_set_user_remind_for_event():
    result = admin_interface.set_user_remind_for_event(event_info['event_id'], user_id)
    u_ids = admin_interface.get_users_remind_by_event(event_info['event_id'])
    assert result == 1 and user_id in u_ids

def test_reset_user_remind_for_event():
    result = admin_interface.set_user_remind_for_event(event_info['event_id'], user_id)
    u_ids = admin_interface.get_users_remind_by_event(event_info['event_id'])
    assert result == 0 and user_id in u_ids

def test_cleare_db_end():
    admin_interface.del_conf(conf_info['conf_id'])
    admin_interface.del_conf(conf_info2['conf_id'])
    admin_interface.del_conf(conf_info3['conf_id'])
    admin_interface.del_event(event_info['event_id'])
    admin_interface.del_event(event_info2['event_id'])
    all_confs = admin_interface.get_all_confs()
    all_events = admin_interface.get_all_events()
    all_themes = admin_interface.get_all_themes()
    assert (conf_info['conf_id'] in all_confs or conf_info2['conf_id'] in all_confs or\
        conf_info3['conf_id'] in all_confs or event_info['event_id'] in all_events or\
        event_info2['event_id'] in all_events or 'test_theme' in all_themes) is False