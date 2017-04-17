import unittest
from unittest.mock import patch

from cool_story_bot.bots.base_bot import BaseBot


class BaseBotTest(unittest.TestCase):

    def setUp(self):
        with patch.object(BaseBot, '_get_content', return_value="Test Content"):
            self.base_bot = BaseBot()
            self.assertEqual(self.base_bot.content, "Test Content")

    def test_base_bot_content(self):
        with self.assertRaises(NotImplementedError):
            BaseBot()

    @patch('twitter.Api.PostUpdate')
    def test_base_bot_post_status(self, post_update):
        post_update.return_value = "update"
        self.assertEqual("update", self.base_bot.post_status())
