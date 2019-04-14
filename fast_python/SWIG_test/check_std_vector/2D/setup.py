#!/usr/bin/env python3

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


example_module = Extension('_test',
                           sources=['test_wrap.cxx', 'test.cpp'],
                           )

setup (name = 'test',
       version = '0.1',
       author      = "SWIG Doc",
       description = """using std_vector""",
       ext_modules = [example_module],
       py_modules = ["test"],
       )
