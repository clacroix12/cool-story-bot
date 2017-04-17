import wikipedia
from wikipedia import DisambiguationError

from cool_story_bot.bots.base_bot import BaseBot
from cool_story_bot.utils.log import logger
from cool_story_bot.utils.retry import retry

CHAR_LIMIT = 140


class WikiBot(BaseBot):
    def __init__(self):
        super(WikiBot, self).__init__()

    def _get_content(self):
        """
        Retrieves content to be used for status updates.

        :return: content
        """
        logger.info("Retrieving content from Wikipedia.")
        return self._validated_content()

    def _validated_content(self):
        """
        Retrieves content and ensures it does not exceed the character limit.

        :return: content
        """
        content = None
        while not content:
            first = self._get_random_wiki_sentence()
            logger.info("content length: {}".format(len(first)))
            if len(first) <= CHAR_LIMIT:
                content = first
            else:
                logger.warning("Content length greater than limit, retrieving new content.")
        return content

    @staticmethod
    @retry(DisambiguationError)
    def _get_random_wiki_sentence():
        """
        Retrieves the first sentence from a random wikipedia article.
        If a DisambiguationError occurs, raise it which causes triggers a retry.

        :return: first sentence of a random wikipedia article
        """
        try:
            return wikipedia.summary(wikipedia.random(), sentences=1)
        except DisambiguationError:
            raise
