#!/usr/bin/env python3.5

import telegram
from telegram.ext import Updater, CommandHandler, updater

class NotificationBot():

    def start(self, bot, update):
        if not self.is_authorized(bot, update):
            return
        self.send_message(update.message.chat_id, text='Hello World!')

    def hello(self, bot, update):
        if not self.is_authorized(bot, update):
            return
        self.send_message(update.message.chat_id, text='Hello {0}'.format(update.message.from_user.first_name))

    def send_message(self, chat_id, text, **args):
        self.bot.send_message(chat_id=chat_id, text=text, **args)
        self.sendMessages += 1

    def is_authorized(self, bot, update):
        authorized_users = [x['telegram_chat_id'] for x in self.cfg["users"].values() if 'telegram_chat_id' in x]
        if update.message.chat_id not in authorized_users:
            self.send_message(update.message.chat_id, text='Unauthorized: %d' % update.message.chat_id)
            return False
        return True

    def __init__(self, config):
        self.cfg = config
        
        self.ready = False
        self.sendMessages = 0

        # Cerate the Telegram bot
        self.bot = telegram.Bot(token=self.cfg['bot_token'])
        self.updater = Updater(bot=self.bot)

        # Get the dispatcher to register handlers
        self.dispatcher = self.updater.dispatcher

        if self.dispatcher is not None:
            self.dispatcher.add_handler(CommandHandler('start', self.start))
            self.dispatcher.add_handler(CommandHandler('hello', self.hello))
            self.ready = True
        
        print('Telegram bot active')
        
        # Start polling
        self.updater.start_polling(clean=True, timeout=30)
        self.updater.idle()