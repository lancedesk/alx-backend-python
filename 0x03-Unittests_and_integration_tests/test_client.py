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


if __name__ == '__main__':
    unittest.main()
