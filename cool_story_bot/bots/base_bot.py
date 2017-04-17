import json
import os

import twitter

from cool_story_bot import MAIN_MODULE
from cool_story_bot.utils.log import logger


class BaseBot(object):
    """
    Base class for Story Bots
    Children must implement the get_content method.
    """

    def __init__(self):
        self.api = self._connect()
        self.content = self._get_content()

    def post_status(self):
        """
        Posts a status update to the bot's twitter account.
        """
        logger.info("Posting status update: {}".format(self.content))
        status_update = self.api.PostUpdate(self.content)
        logger.info("Success. Cool story bot!")
        return status_update

    def _get_content(self):
        """
        Method to retrieve content to be used in status updates.
        """
        raise NotImplementedError

    def _connect(self):
        """
        Connect to the twitter API

        :return: twitter api object
        """
        config = self._get_config()
        api = twitter.Api(consumer_key=config['consumer_key'],
                          consumer_secret=config['consumer_secret'],
                          access_token_key=config['access_token_key'],
                          access_token_secret=config['access_token_secret'])
        return api

    @staticmethod
    def _get_config():
        config_file = os.path.join(MAIN_MODULE, 'config.json')
        with open(config_file) as cfg:
            data = json.load(cfg)
        return data
