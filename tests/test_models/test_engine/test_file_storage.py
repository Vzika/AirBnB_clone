#!/usr/bin/python3
"""
test_file_storage module: A unittest subclass for testing file_storage module
"""

from models.engine import file_storage
import inspect
import unittest


class Test_FileStorage(unittest.TestCase):
    """
    Test_FileStorage: (class) - unittest subclass to run test cases
    on file_storage
    """
    @classmethod
    def setUp(cls):
        """
        setUp: (class method) - method for sharing resources across all methods

        setup: assigned with a list of all the functions in FileStorage
        """
        cls.setup = inspect.getmembers(file_storage.FileStorage,
                                       inspect.isfunction)

    def test_module_docs(self):
        """
        test for module docstring
        """
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docs(self):
        """
        test for class docstring
        """
        self.assertTrue(len(file_storage.FileStorage.__doc__) >= 1)

    def test_function_docs(self):
        """
        test for functions docstrings
        """
        for each_func in self.setup:
            self.assertTrue(len(each_func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
