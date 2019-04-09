#!/usr/bin/env python3

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


example_module = Extension('_example',
                           sources=['example_wrap.cxx', 'example.cpp'], language='c++', swig_opts = ['-c++'])

setup (name = 'example',
       version = '0.1',
       author      = "SWIG Doc",
       description = """using std_string""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )
