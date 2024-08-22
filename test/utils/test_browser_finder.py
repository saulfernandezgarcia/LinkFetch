from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.utils.browser_finder import BrowserFinder

class TestBrowserFinder(TestCase):
    
    @patch("src.utils.browser_finder.psutil.process_iter")
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
        self.assertTrue(BrowserFinder.is_browser_active("chrome.exe"))

    @patch("src.utils.browser_finder.psutil.process_iter")
    def test_is_browser_active_when_process_does_not_exist(self, mock_process_iter):
        mock_process = MagicMock()
        mock_process.info = {"name" : "undesiredBrowser.exe"}
        mock_process_iter.return_value = [mock_process]

        self.assertFalse(BrowserFinder.is_browser_active("chrome.exe"))

    @patch("src.utils.browser_finder.psutil.process_iter")
    def test_is_browser_active_when_no_process(self, mock_process_iter):
        mock_process_iter.return_value = []
        self.assertFalse(BrowserFinder.is_browser_active("chrome.exe"))

    @patch("src.utils.browser_finder.psutil.process_iter")
    def test_is_browser_active_when_process_is_none(self, mock_process_iter):
        mock_process_iter.return_value = []
        self.assertFalse(BrowserFinder.is_browser_active("chrome.exe"))

    @patch("src.utils.browser_finder.psutil.process_iter")
    def test_active_browsers(self, mock_process_iter):
        mock_process = MagicMock()
        mock_process.info = {"name":"chrome.exe"}
        mock_process_iter.return_value = [mock_process]

        self.assertDictEqual(BrowserFinder.active_browsers(), {"chrome.exe":"Chrome"})