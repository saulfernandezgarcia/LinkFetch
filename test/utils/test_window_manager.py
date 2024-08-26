from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.utils.window_manager import WindowManager

class TestWindowManager(TestCase):

    '''
    Important: patch order is important! The uppermost patch is the rightmost parameter!
    '''
    @patch("src.utils.window_manager.WindowManager.previous_tab")
    @patch("src.utils.window_manager.WindowManager.next_tab")
    @patch("src.utils.window_manager.WindowManager.copy_paste_link")
    @patch("pygetwindow.Window")
    def test_obtain_tabs_when_no_repeated_links(self, mock_window, mock_copy_paste_link, mock_next_tab, mock_previous_tab):

        mock_window.maximize = MagicMock()
        mock_window.minimize = MagicMock()
        mock_next_tab = MagicMock()
        mock_previous_tab = MagicMock()

        captured_tabs = [
            "https://saulfernandezgarcia.github.io",
            "https://www.google.com",
            "https://www.youtube.com",
            "https://saulfernandezgarcia.github.io"
        ]

        expected_tabs = ["https://saulfernandezgarcia.github.io",
                            "https://www.google.com",
                            "https://www.youtube.com"]

        mock_copy_paste_link.side_effect = captured_tabs

        result = WindowManager.obtain_tabs(mock_window)

        self.assertListEqual(result, expected_tabs)

    @patch("src.utils.window_manager.WindowManager.previous_tab")
    @patch("src.utils.window_manager.WindowManager.next_tab")
    @patch("src.utils.window_manager.WindowManager.copy_paste_link")
    @patch("pygetwindow.Window")
    def test_obtain_tabs_when_repeated_links_first_last(self, mock_window, mock_copy_paste_link, mock_next_tab, mock_previous_tab):
        mock_window.maximize = MagicMock()
        mock_window.minimize = MagicMock()
        mock_next_tab = MagicMock()
        mock_previous_tab = MagicMock()

        captured_tabs = [
            "https://saulfernandezgarcia.github.io",
            "https://www.google.com",
            "https://www.youtube.com",
            "https://saulfernandezgarcia.github.io",
            "https://saulfernandezgarcia.github.io"
        ]

        expected_tabs = ["https://saulfernandezgarcia.github.io",
                            "https://www.google.com",
                            "https://www.youtube.com"]

        mock_copy_paste_link.side_effect = captured_tabs

        result = WindowManager.obtain_tabs(mock_window)

        self.assertListEqual(result, expected_tabs)

    @patch("src.utils.window_manager.WindowManager.previous_tab")
    @patch("src.utils.window_manager.WindowManager.next_tab")
    @patch("src.utils.window_manager.WindowManager.copy_paste_link")
    @patch("pygetwindow.Window")
    def test_obtain_tabs_when_repeated_links_first_middle(self, mock_window, mock_copy_paste_link, mock_next_tab, mock_previous_tab):

        mock_window.maximize = MagicMock()
        mock_window.minimize = MagicMock()
        mock_next_tab = MagicMock()
        mock_previous_tab = MagicMock()

        captured_tabs = ["https://saulfernandezgarcia.github.io",
                            "https://www.google.com",
                            "https://www.youtube.com",
                            "https://saulfernandezgarcia.github.io",
                            "https://www.google.com/maps"]

        expected_tabs = ["https://saulfernandezgarcia.github.io",
                         "https://www.google.com",
                         "https://www.youtube.com",
                         "https://www.google.com/maps"]

        mock_copy_paste_link.side_effect = captured_tabs

        result = WindowManager.obtain_tabs(mock_window)

        self.assertListEqual(result, expected_tabs)

    def test_next_tab(self):
        # No idea how to test this.
        pass

    @patch("pyperclip.paste", return_value="https://saulfernandezgarcia.github.io")
    def test_copy_paste_link(self, mock_paste):
        testUrl = "https://saulfernandezgarcia.github.io"
        self.assertEquals(WindowManager.copy_paste_link(), testUrl)