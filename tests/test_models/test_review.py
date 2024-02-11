#!/usr/bin/python3
"""
test_review module: A unittest subclass for testing review module
"""

from models import review
import inspect
import unittest


class TestReview(unittest.TestCase):
    """TestReview: (class) - unittest subclass to run test cases on review
    """
    @classmethod
    def setUp(cls):
        """
        setUp: (class method) - method for sharing resources across all methods

        setup: assigned with a list of all the functions in BaseModel
        """
        cls.setup = inspect.getmembers(review.BaseModel,
                                       inspect.isfunction)

    def test_module_docs(self):
        """
        test for module docstring
        """
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docs(self):
        """
        test for class docstring
        """
        self.assertTrue(len(review.BaseModel.__doc__) >= 1)

    def test_function_docs(self):
        """
        test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
