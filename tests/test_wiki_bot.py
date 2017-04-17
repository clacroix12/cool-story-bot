import logging
import random
import string
import unittest
from unittest.mock import patch

from wikipedia import DisambiguationError

from cool_story_bot.bots.wiki_bot import WikiBot
from cool_story_bot.utils.log import logger


class WikiBotTest(unittest.TestCase):

    def test_wiki_bot(self):
        with patch.object(WikiBot, '_get_content', return_value="Test Content"):
            wiki_bot = WikiBot()
            self.assertEqual(wiki_bot.content, "Test Content")

    def test_get_content(self):
        with patch.object(WikiBot, '_validated_content', return_value="Validated Content"):
            wiki_bot = WikiBot()
            self.assertEqual(wiki_bot.content, "Validated Content")

    @patch('wikipedia.summary')
    def test_get_random_wiki_sentence(self, summary):
        summary.return_value = "Summary"
        wiki_bot = WikiBot()
        self.assertEqual(wiki_bot.content, "Summary")

    @patch('wikipedia.summary')
    def test_get_random_wiki_sentence_error(self, summary):
        summary.side_effect = DisambiguationError(title="TestTitle", may_refer_to="A")
        with self.assertRaises(DisambiguationError):
            WikiBot()

    def test_validated_content(self):
        with patch.object(WikiBot, '_get_random_wiki_sentence', return_value="Random Sentence"):
            wiki_bot = WikiBot()
            self.assertEqual(wiki_bot.content, "Random Sentence")

    def test_validated_content_exceeds_char_limit(self):
        long_string = ''.join(random.choice(string.ascii_letters) for _ in range(141))
        short_string = ''.join(random.choice(string.ascii_letters) for _ in range(20))
        print(len(long_string))
        print(len(short_string))
        test_strings = [long_string, short_string]
        with patch.object(WikiBot, '_get_random_wiki_sentence', side_effect=test_strings):
            wiki_bot = WikiBot()
            self.assertLogs(logger=logger, level=logging.WARNING)
            self.assertEqual(wiki_bot.content, short_string)
