#!/usr/bin/env python3.5

import telegram
from telegram.ext import Updater, CommandHandler, updater
from user import User
from datetime import datetime
import logging

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
        for user in self.users:
            if user.telegram_chat_id == update.message.chat_id:                
                return True
        self.send_message(update.message.chat_id, text='Unauthorized: %d' % update.message.chat_id)
        return False

    def send_startup_nofitication(self):
        for user in self.users:
            if user.is_member_of_group('admin'):
                self.send_message(user.telegram_chat_id, text='Startup: ' + datetime.now().strftime('%a %d. %b - %H:%M'))

    def __init__(self, job_manager, users, token):
        self.job_manager = job_manager        
        self.users = users
        self.token = token
        self.logger = logging.getLogger(__name__)
        
        self.ready = False
        self.sendMessages = 0

        self.logger.info('Startup')
        self.logger.debug('Bot token: ' + token)        

        # Create the Telegram bot
        self.logger.info('Create the Telegram bot')
        self.bot = telegram.Bot(token=self.token)
        self.updater = Updater(bot=self.bot)


        # Get the dispatcher to register handlers
        self.dispatcher = self.updater.dispatcher

        self.logger.info('Register handlers')
        if self.dispatcher is not None:
            self.dispatcher.add_handler(CommandHandler('start', self.start))
            self.dispatcher.add_handler(CommandHandler('hello', self.hello))
            self.ready = True
        
        self.logger.info('Telegram bot active')       
        