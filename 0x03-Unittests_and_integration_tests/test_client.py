#!/usr/bin/env python3

"""Module defines unittest.TestCase test classes for module client.py"""

import unittest
from unittest.mock import MagicMock, Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for client.GithubOrgClient class"""

    @parameterized.expand(
        [
            ("google", {"status": "ok"}),
            ("abc", {}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, input, expected, mocked_get_json):
        """Test method for client.GithubOrgClient.org"""
        test_obj = GithubOrgClient(input)
        mocked_get_json.return_value = MagicMock(return_value=expected)
        self.assertEqual(test_obj.org(), expected)
        mocked_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{input}"
                )


if __name__ == "__main__":
    unittest.main()
