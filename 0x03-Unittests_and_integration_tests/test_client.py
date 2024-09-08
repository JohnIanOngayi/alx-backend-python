#!/usr/bin/env python3

"""Module defines unittest.TestCase test classes for module client.py"""

import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    def test_public_repos_url(self):
        """Test client.GithubOrgClient.public_repos_url"""
        with patch("client.GithubOrgClient._public_repos_url", "Success"):
            test_obj = GithubOrgClient("google")
            self.assertEqual(test_obj._public_repos_url, "Success")

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        """Tests GithubOrgClient.public_repos"""
        list_of_repos = TEST_PAYLOAD[0][1]
        with patch("client.GithubOrgClient._public_repos_url", list_of_repos):
            test_obj = GithubOrgClient("google")
            mocked_get_json.return_value = MagicMock(
                    return_value={"status": "ok"}
                    )
            self.assertEqual(test_obj.org(), {"status": "ok"})
        mocked_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/google"
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
