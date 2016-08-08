import logging
import logging.config    
import glob
import json

from bot import NotificationBot
from user import User  
from job import Job

class JobManager():
    """description of class"""

    def __init__(self, config):
        self.cfg = config
        self.users = list()
        self.jobs = list()
        self.bot = None
        self.logger = logging.getLogger(__name__)    

        # init users list
        self.logger.info("Initialize user:")
        for user_config in config['users'].items():
            self.logger.info('{0}'.format(user_config[0]))
            self.users.append(User(user_config))
        
        # init jobs
        self.logger.info("Initialize jobs:")  
        self.job_path = config['job_folder']
        for job_config in glob.iglob(self.job_path + '/*.job.json', recursive=True):
            with open(job_config) as fp:
                job_config = json.load(fp)                
                self.logger.info('{0}'.format(job_config['name']))
                self.jobs.append(Job(job_config))

        # init notification bot
        self.logger.info("Initialize notification bot")   
        self.bot = NotificationBot(self, self.users, self.cfg['bot_token'])
        self.bot.send_startup_nofitication()

        # Start polling
        self.logger.info("Start polling") 
        self.bot.updater.start_polling(clean=True, timeout=30)
        self.bot.updater.idle()


