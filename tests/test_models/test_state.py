#!/usr/bin/python3
"""
test_state module: A unittest subclass for testing state module
"""

from models import state
import inspect
import unittest


class Teststate(unittest.TestCase):
    """
    Teststate: (class) - unittest subclass to run test cases on state
    """
    @classmethod
    def setUp(cls):
        """
        setUp: (class method) - method for sharing resources across all methods
        """
        cls.setup = inspect.getmembers(state.BaseModel,
                                       inspect.isfunction)

    def test_module_docs(self):
        """
        test for module docstring
        """
        self.assertTrue(len(state.__doc__) >= 1)

    def test_class_docs(self):
        """
        test for class docstring
        """
        self.assertTrue(len(state.BaseModel.__doc__) >= 1)

    def test_function_docs(self):
        """
        test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
