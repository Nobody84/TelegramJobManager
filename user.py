class User():
    """description of class"""


    def __init__(self, user_config):
        self.name = user_config[0]
        self.telegram_chat_id = user_config[1]['telegram_chat_id']
        self.groups = user_config[1]['groups']
        self.cfg = user_config

    def is_member_of_group(self, groupname):
        if groupname in self.groups:
            return True
        return False