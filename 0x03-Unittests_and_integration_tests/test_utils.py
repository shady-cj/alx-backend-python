#!/usr/bin/env python3
"""
Writing testcase form the utils.py module.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """
    Testing the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Writing test cases for the test access nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, key):
        """
        Testing access_nested_map for when it raises exccption
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertIn(key, str(e.exception))


class TestGetJson(unittest.TestCase):
    """
    Tests the get_json() function in the utils module
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Testing the get_json() function and also patching the
        request.get library.
        """
        with patch('utils.requests') as requests:
            mock_response = MagicMock()
            mock_response.json.return_value = {"test_payload": test_payload}
            requests.get.return_value = mock_response
            self.assertEqual(get_json(test_url).get("test_payload"), test_payload)
