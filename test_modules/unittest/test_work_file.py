"""
File: test_work_file.py
Author: Kazantsev Andrey
Email: kaz.prao@bk.ru
Github: https://github.com/KazAndr
Description: file for testing work functions from work_file
"""

import unittest
import work_file


class TestWorkfile(unittest.TestCase):
    """
    Class for testing
    """
    def test_add(self):
        """
        Testing method for add function
        """
        self.assertEqual(work_file.add(10, 5), 15)
        self.assertEqual(work_file.add(-1, 1), 0)
        self.assertEqual(work_file.add(-1, -1), -2)

    def test_subtract(self):
        """
        Testing method for subtract function
        """
        self.assertEqual(work_file.subtract(10, 5), 5)
        self.assertEqual(work_file.subtract(-1, 1), -2)
        self.assertEqual(work_file.subtract(-1, -1), 0)

    def test_multiply(self):
        """
        Testing method for multiply function
        """
        self.assertEqual(work_file.multiply(10, 5), 50)
        self.assertEqual(work_file.multiply(-1, 1), -1)
        self.assertEqual(work_file.multiply(-1, -1), 1)

    def test_devide(self):
        """
        Testing method for devide function
        """
        self.assertEqual(work_file.devide(10, 5), 2)
        self.assertEqual(work_file.devide(-1, 1), -1)
        self.assertEqual(work_file.devide(-1, -1), 1)
        self.assertEqual(work_file.devide(5, 2), 2.5)

        self.assertRaises(ValueError, work_file.devide, 10, 0)


if __name__ == '__main__':
    unittest.main()
