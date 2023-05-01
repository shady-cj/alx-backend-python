#!/usr/bin/env python3
"""
Writing testcase for the clients.py module.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing the GithubOrgClient Class
    """

    @parameterized.expand([
        ("google", {'test_payload': True}),
        ("abc", {"test_payload": False})
    ])
    @patch("client.get_json")
    def test_org(self, test_input, expected, mock_get_json):
        """
        testing the org method in the GithubOrgClient class.
        """
        github_client = GithubOrgClient(test_input)
        mock_get_json.return_value = expected
        self.assertEqual(github_client.org, expected)
        self.assertEqual(github_client.org, expected)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """
        Testing the _public_repos_url from the GithubOrgClient
        class
        """
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock)\
        as mock_gitclient_org:
            payload = {"repos_url": ["abc", "def", "ghi"]}
            mock_gitclient_org.return_value = payload
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client._public_repos_url, payload.get('repos_url'))
