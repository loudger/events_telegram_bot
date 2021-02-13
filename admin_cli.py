from admin_API import admin_interface
import cmd


class bot_shell(cmd.Cmd):
    intro = 'Welcome, bot_shell!\nType help or ? to list commands\n'
    prompt = 'hangout_bot_shell:'

    def parse_arg(self, args):
        args = args.split()
        return args

    def do_get_all_confs(self, args):
        '''get all confs. No parameters needed'''
        result = admin_interface.get_all_confs()
        print(result)

    def do_get_all_events(self, args):
        '''get all events. No parameters needed'''
        result = admin_interface.get_all_events()
        print(result)

    def do_get_all_themes(self, args):
        '''get all events themes. No parameters needed'''
        result = admin_interface.get_all_themes()
        print(result)

    def do_get_users_by_event(self, args):
        '''get users who go to the event.
        get_user_by_event <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.get_users_by_event(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_users_remind_by_event(self, args):
        '''get users going to an event who need a remind.
        get_users_remind_by_event <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.get_users_remind_by_event(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_event_name(self, args):
        '''get event name
        get_event_name <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.get_event_name(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_event_descr(self, args):
        '''get event descr
        get_event_descr <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.get_event_descr(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_event_url(self, args):
        '''get event url
        get_event_url <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.get_event_url(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_event_date(self, args):
        '''get event date
        get_event_date <event_id>'''
        args = self.parse_arg(args)
        event_id = args[0]
        result = admin_interface.get_event_date(event_id)
        print(result)

    def do_get_event_theme(self, args):
        '''get event theme
        get_event_theme <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.get_event_theme(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_subconf_by_conf_event(self, args):
        '''get subconf by conf and event
        get_event_theme <conf_id> <event_id>'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            event_id = args[1]
            result = admin_interface.get_subconf_by_conf_event(conf_id, event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_conf_options(self, args):
        '''get conf options
        get_conf_options <conf_id>'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            result = admin_interface.get_conf_options(conf_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_get_conf_filter(self, args):
        '''get conf filter
        get_conf_filter <conf_id>'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            result = admin_interface.get_conf_filter(conf_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')


    def do_add_event(self, args):
        '''add info abount event
        add_event <event_id> <event_name> <event_descr> <event_url> <event_date> <event_theme1> [<event_theme2> .. <event_themeN>]
        '''
        args = self.parse_arg(args)
        try:
            event_info = {'event_id':args[0],'event_name':args[1],'event_descr':args[2],
            'event_url':args[4],'event_date':args[5],'event_theme':args[6:]}
            result = admin_interface.add_event(event_info)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_event_id(self, args):
        '''set event_id
        set_event_id <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.set_event_id(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_event_name(self, args):
        '''set event_name by event_id
        set_event_name <event_id> <event_name>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            event_name = args[1]
            result = admin_interface.set_event_name(event_id, event_name)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_event_descr(self, args):
        '''set event_descr by event_id
        set_event_descr <event_id> <event_descr>'''
        args = self.parse_arg(args)
        event_id = args[0]
        event_descr = args[1]
        result = admin_interface.set_event_descr(event_id, event_descr)
        print(result)

    def do_set_event_url(self, args):
        '''set event_url by event_id
        set_event_url <event_id> <event_url>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            event_url = args[1]
            result = admin_interface.set_event_url(event_id, event_url)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_event_date(self, args):
        '''set event_date by event_id
        set_event_date <event_id> <event_date>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            event_date = args[1]
            result = admin_interface.set_event_date(event_id, event_date)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_event_theme(self, args):
        '''set event_theme by event_id
        set_event_theme <event_id> <event_theme>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            event_theme = args[1]
            result = admin_interface.set_event_theme(event_id, event_theme)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_add_conf(self, args):
        '''add info abount conf
        add_conf <conf_id> [<conf_options> <conf_theme1> <conf_theme2> .. <conf_themeN>]'''
        args = self.parse_arg(args)
        try:
            conf_info = {'conf_id':args[0],'conf_options':args[1],'conf_themes':args[2:]}
            result = admin_interface.add_conf(conf_info)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_conf_id(self, args):
        '''set conf_id
        set_conf_id <conf_id>'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            result = admin_interface.set_conf_id(conf_id)
            # if result == 1:
            #     print('Success')
            # elif result == 0:
            #     print('Already exist')
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_options_for_conf(self, args):
        '''set options for conf by conf_id.
        set_options_for_conf <conf_id> <conf_options>
        conf_options = [0|1][0|1][0|1]
        [activate bot][create subconf][filter cost off/on]
        for example 000 or 101'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            conf_options = args[1]
            result = admin_interface.set_options_for_conf(conf_id, conf_options)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_filter_for_conf(self, args):
        '''set filter for conf by conf_id.
        set_filter_for_conf <conf_id> <conf_filter>'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            conf_filter = args[1]
            result = admin_interface.set_filter_for_conf(conf_id, conf_filter)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_subconf_for_conf_event(self, args):
        '''set subconf for conf by conf_id and event_id.
        set_subconf_for_conf <conf_id> <event_id> <conf_subconf>'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            event_id = args[1]
            subconf_url = args[2]
            result = admin_interface.set_subconf_for_conf_event(conf_id, event_id, subconf_url)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_user_for_event(self, args):
        '''set user for event by event_id.
        set_filter_for_conf <event_id> <user_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            user_id = args[1]
            result = admin_interface.set_user_for_event(event_id, user_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_set_user_remind_for_event(self, args):
        '''set users going to an event who need a remind by event_id.
        set_user_remind_for_event <event_id> <user_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            user_id = args[1]
            result = admin_interface.set_user_remind_for_event(event_id, user_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')


    def do_del_conf(self, args):
        '''delete all info abount conf by conf_id.
        del_conf <conf_id>'''
        args = self.parse_arg(args)
        try:
            conf_id = args[0]
            result = admin_interface.del_conf(conf_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_del_event(self, args):
        '''delete all info abount event by event_id.
        del_event <event_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            result = admin_interface.del_event(event_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_del_user_for_event(self, args):
        '''delete info abount user by event_id and user_id.
        del_user_for_event <event_id> <user_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            user_id = args[1]
            result = admin_interface.del_user_for_event(event_id ,user_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

    def do_del_user_remind_for_event(self, args):
        '''delete info abount user_remind by event_id and user_id.
        del_user_remind_for_event <event_id> <user_id>'''
        args = self.parse_arg(args)
        try:
            event_id = args[0]
            user_id = args[1]
            result = admin_interface.del_user_remind_for_event(event_id ,user_id)
            print(result)
        except IndexError:
            print('Incorrect parametrs')

if __name__ == '__main__':
    bot_shell().cmdloop()