import unittest

from cool_story_bot.utils.retry import retry


class TestRetry(unittest.TestCase):
    def setUp(self):
        self.attempts = 0

    def test_retry_no_retry(self):
        self.wrapped_method(False)
        self.assertEqual(self.attempts, 1)

    def test_retry_fail(self):
        with self.assertRaises(ValueError):
            self.wrapped_method(True)
        self.assertEqual(self.attempts, 3)

    @retry(ValueError, tries=3, delay=0)
    def wrapped_method(self, raise_exception):
        self.attempts += 1
        if raise_exception:
            raise ValueError('Something went wrong')
