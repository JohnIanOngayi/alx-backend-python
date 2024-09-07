#!/usr/bin/env python3

"""
Module utilises unittest python module to test utils.py
"""

from typing import Mapping, Union
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class defines unittest methods for method utils.access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: tuple, expected: Union[int, Mapping]
    ) -> None:
        """Tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: tuple
    ) -> None:
        """Tests the access_nested_map KeyError exception"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class defines unittest methods for method utils.get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Mapping) -> None:
        """Tests the get_json method"""
        with patch("requests.get") as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            json = get_json(test_url)
            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(json, test_payload)


class TestMemoize(unittest.TestCase):
    """Class defines unittest test methods for method utils.memoize"""

    def test_memoize(self):
        """Tests the memoize method"""

        class TestClass:
            """Test class for memoize"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()
        with patch.object(TestClass, "a_method", return_value=42) as mock_obj:
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            mock_obj.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
