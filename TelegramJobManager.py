#!/usr/bin/env python3.5

import sys
import json
import logging
from user import User
from jobmanager import JobManager

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

    print('config')
    print(config)
    
    # initialize the job manager
    manger = JobManager(config)
    

if __name__ == '__main__':
    main()