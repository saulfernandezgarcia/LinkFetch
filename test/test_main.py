from unittest import TestCase
from unittest.mock import patch, MagicMock, call

import datetime
import os

from src.main import create_timestamped_file

class TestMainFunctions(TestCase):

    @patch("builtins.open", new_callable=MagicMock)
    @patch("src.main.os.makedirs")
    @patch("src.main.datetime")
    def test_create_timestamped_file(self, mock_datetime, mock_makedirs: MagicMock, mock_open: MagicMock):

        # Mock datetime to return a specific date and time
        mock_datetime.datetime.now.return_value = datetime.datetime(2024, 8, 26, 17, 0, 0)
        mock_datetime.datetime.strftime.return_value = "20240826_170000"

        content_list = [
            "https://saulfernandezgarcia.github.io",
            "https://www.google.com",
            "https://www.youtube.com"
        ]

        expected_filepath = os.path.join("LinkFetch_Results", f"URL_LIST_{mock_datetime.datetime.strftime.return_value}.txt")

        result_filepath = create_timestamped_file(content_list)

        mock_makedirs.assert_called_once_with("LinkFetch_Results")

        # https://docs.python.org/3/library/unittest.mock.html
        mock_open.assert_called_once_with(expected_filepath, "w")

        mock_file_handle = mock_open()

        self.assertEqual(result_filepath, expected_filepath)


        '''
        # Still figuring out how to test for the writing calls
        expected_write_calls = [
            call("https://saulfernandezgarcia.github.io\n"),
            call("https://www.google.com\n"),
            call("https://www.youtube.com")
        ]
        mock_file_handle.write.assert_has_calls(?)
        '''






