#!/usr/bin/env python3.5

import sys
import json
import logging
from bot import NotificationBot

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
    NotificationBot(config)

if __name__ == '__main__':
    main()