#!/usr/bin/env python3
"""
Writing testcase for the clients.py module.
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing the GithubOrgClient Class
    """

    @parameterized.expand(
        [("google", {"test_payload": True}), ("abc", {"test_payload": False})]
    )
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
        mock_get_json.assert_called_with(f"https://api.github.com/orgs/{test_input}")

    def test_public_repos_url(self):
        """
        Testing the _public_repos_url from the GithubOrgClient
        class
        """
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_gitclient_org:
            payload = {"repos_url": "abc"}
            mock_gitclient_org.return_value = payload
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client._public_repos_url, payload.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Testing the public_repos from the GithubOrgClient class
        """
        mock_get_json.return_value = [{"name": "abc"}, {"name": "def"}]
        with patch(
            "client.GithubOrgClient._public_repos_url", new_callable=PropertyMock
        ) as mock_pub_repo_url:
            mock_pub_repo_url.return_value = "abc"
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client.public_repos(), ["abc", "def"])
            mock_pub_repo_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, test_repo, test_license_key, expected):
        """
        Testing the has_license method on the GithubOrgClient class
        """

        self.assertEqual(
            GithubOrgClient.has_license(test_repo, test_license_key), expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """
        Setting up the class for the integration tests
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_object = cls.get_patcher.start()
        cls.mock_object.side_effect = cls.side_effect

    @classmethod
    def side_effect(cls, url, *args, **kwargs):
        """
        Controlling the side effect of the mock object
        """
        mock = MagicMock()

        if url == "https://api.github.com/orgs/google":
            mock.json.return_value = cls.org_payload
        elif url == "https://api.github.com/orgs/google/repos":
            mock.json.return_value = cls.repos_payload
        mock.status_code.return_value = 200
        return mock

    @classmethod
    def tearDownClass(cls):
        """
        Tearing down the class after the integration tests
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Testing the public_repos method of the GithubOrgClient class
        """
        github_client = GithubOrgClient("google")
        self.assertEqual(github_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Testing the public_repos method of the GithubOrgClient class with a license
        """
        github_client = GithubOrgClient(
            "google",
        )
        self.assertEqual(github_client.public_repos("apache-2.0"), self.apache2_repos)
