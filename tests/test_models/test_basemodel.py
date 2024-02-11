#!/usr/bin/python3
"""
test_base_model module: Unittest subclass for testing the base_model module
"""

from models import base_model
import inspect
import unittest


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel: Unittest subclass for running test cases on the base_model
    """

    @classmethod
    def setUp(cls):
        """
        setUp: Class method for sharing resources across all methods

        setup: assigned with a list of all the functions in BaseModel
        """
        cls.setup = inspect.getmembers(
            base_model.BaseModel, inspect.isfunction)

    def test_module_docs(self):
        """
        Test for module docstring
        """
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docs(self):
        """
        Test for class docstring
        """
        self.assertTrue(len(base_model.BaseModel.__doc__) >= 1)

    def test_function_docs(self):
        """
        Test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
