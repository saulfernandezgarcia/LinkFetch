from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.browser_finder import BrowserFinder

class TestBrowserFinder(TestCase):

    # setUp executes before every test case
    def setUp(self):
        self.bw = BrowserFinder("chrome.exe")

    def test_init_when_browser_is_none(self):
        with self.assertRaises(ValueError):
            BrowserFinder(None)

    def test_choose_browser(self):
        self.bw.choose_browser("chrome.exe")
        self.assertEqual(self.bw.desired_browser, "chrome.exe")
    @patch("src.browser_finder.psutil.process_iter")
    def test_is_browser_active_when_process_exists(self, mock_process_iter):
        mock_process = MagicMock()
        mock_process.info = {"name" : "chrome.exe"}
        mock_process_iter.return_value = [mock_process] # Because process_iter returns a list of dictionaries

        '''
        The patch will replace the process_iter with a MagicMock object for this function
        only. Thus, we will be mocking the process_iter process.
        When "bw.is_browser_active()" is called, inside of it there are occurences
        of "process_iter" being used; rather than actually calling the real code, it
        will resort to the mock we created.
        mock_process_iter is a MagicMock.
        mock_process_iter.return_value ALSO is a MagicMock.
        '''
        self.assertTrue(self.bw.is_browser_active())
        self.assertTrue(self.bw.browser_is_active)

    @patch("src.browser_finder.psutil.process_iter")
    def test_is_browser_active_when_process_does_not_exist(self, mock_process_iter):
        mock_process = MagicMock()
        mock_process.info = {"name" : "undesiredBrowser.exe"}
        mock_process_iter.return_value = [mock_process]

        self.assertFalse(self.bw.is_browser_active())
        self.assertFalse(self.bw.browser_is_active)

    @patch("src.browser_finder.psutil.process_iter")
    def test_is_browser_active_when_no_process(self, mock_process_iter):
        mock_process_iter.return_value = []

        self.assertFalse(self.bw.is_browser_active())
        self.assertFalse(self.bw.browser_is_active)

    @patch("src.browser_finder.psutil.process_iter")
    def test_is_browser_active_when_process_is_none(self, mock_process_iter):
        mock_process_iter.return_value = []

        self.assertFalse(self.bw.is_browser_active())
        self.assertFalse(self.bw.browser_is_active)