#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(
                 self, org_name: str,
                 expected_response: Dict,
                 mock_get_json: MagicMock
                ) -> None:
        """
        Test org method of GithubOrgClient class.

        Args:
            org_name (str): The name of the organization.
            expected_response (Dict): The expected response data.
            mock_get_json (MagicMock): Mock object for get_json function.
        """

        mock_get_json.return_value = MagicMock(return_value=expected_response)
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org(), expected_response)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

    def test_public_repos_url(self) -> None:
        """
        Tests the `_public_repos_url` property.
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            public_repos = "https://api.github.com/users/google/repos"
            # Mock the org property to return a known payload
            mock_org.return_value = {
                'repos_url': public_repos,
            }

            # Call the _public_repos_url property and assert the result
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                public_repos,
            )

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        '''Test public_repos method.'''
        # Define the payload to be returned by get_json
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_get_json.return_value = payload

        # Patch the _public_repos_url property to return a known value
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = "world"

            # Call the method under test
            response = GithubOrgClient('test').public_repos()

            # Check if the response matches the expected output
            self.assertEqual(response, ["Google", "TT"])

            # Check if patched property & method were called once each
            mocked_public_repos_url.assert_called_once()
            mocked_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
