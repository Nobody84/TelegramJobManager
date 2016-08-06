#!/usr/bin/env python3.5

import sys
import os
import json
import logging
from user import User
from jobmanager import JobManager
import logging
import logging.config

# Enable telegram bot logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#######################################################################################
#######################################################################################
def main():
    configFilePath = 'config.json'
    if len(sys.argv) < 2:
        print('No config file given, take default path')
    else:
        configFilePath = sys.argv[1]

    with open(configFilePath) as fp:
        config = json.load(fp)
    
    # setup logger
    setup_logging()
        
    # initialize the job manager
    manger = JobManager(config)

def setup_logging(
    default_path='logging.json', 
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level) 

if __name__ == '__main__':
    main()