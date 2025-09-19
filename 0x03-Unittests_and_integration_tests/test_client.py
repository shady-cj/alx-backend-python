#!/usr/bin/env python3
"""
Writing testcase for the clients.py module.
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import utils


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
    @classmethod
    def setUpClass(cls):
        cls.get_patcher()

    @classmethod
    def get_patcher(cls):

        cls.patcher = patch("utils.requests.get")
        cls.mock_object = cls.patcher.start()

    @classmethod
    def side_effect(cls, url_payload):
        mock = MagicMock()
        mock.json.return_value = url_payload
        cls.mock_object = mock
        return cls.mock_object

    @classmethod
    def tearDownClass(cls):
        cls.patcher.stop()

    def test_public_repos(self):
        mock = self.side_effect(self.repos_payload)
        github_client = GithubOrgClient("google")
        # self.assertEqual(github_client.public_repos(), self.repos_payload)
        # print(github_client.public_repos())
