#!/usr/bin/python3
"""
test_amenity module: Unittest subclass for testing the amenity module
"""

from models import amenity
import inspect
import unittest


class TestAmenity(unittest.TestCase):
    """
    TestAmenity: Unittest subclass for running test cases on the amenity module
    """

    @classmethod
    def setUp(cls):
        """
        setUp: Class method for sharing resources across all methods
        """
        cls.setup = inspect.getmembers(amenity.BaseModel, inspect.isfunction)

    def test_module_docs(self):
        """
        Test for module docstring
        """
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_class_docs(self):
        """
        Test for class docstring
        """
        self.assertTrue(len(amenity.BaseModel.__doc__) >= 1)

    def test_function_docs(self):
        """
        Test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
