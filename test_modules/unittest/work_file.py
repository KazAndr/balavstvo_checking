"""
File: work_file.py
Author: Kazantsev Andrey
Email: kaz.prao@bk.ru
Github: https://github.com/KazAndr
Description: file for testing module unittest. There are work functon.
"""


def add(a, b):
    """
    Add function
    """
    return a + b


def subtract(a, b):
    """
    Subtract function
    """
    return a - b


def multiply(a, b):
    """
    Multiply function
    """
    return a * b


def devide(x, y):
    """
    Devide function
    """
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y
