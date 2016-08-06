from bot import NotificationBot
from user import User

class JobManager():
    """description of class"""

    def __init__(self, config):
        self.cfg = config
        self.users = list()
        self.jobs = list()
        self.bot = None
        
        # init users list
        print("Initialize users:")
        for user_config in config['users'].items():
            print('{0}'.format(user_config[0]))
            self.users.append(User(user_config))
        
        # init notification bot
        print("Initialize notification bot")       
        self.bot = NotificationBot(self, self.users, self.cfg['bot_token'])
        self.bot.send_startup_nofitication()

        # Start polling
        self.bot.updater.start_polling(clean=True, timeout=30)
        self.bot.updater.idle()


