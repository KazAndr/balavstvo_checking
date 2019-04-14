#!/usr/bin/env python3

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


arr_check_module = Extension('_arr_check',
                           sources=['arr_check_wrap.cxx', 'arr_check.cpp'],
                           )

setup (name = 'arr_check',
       version = '0.1',
       author      = "Kazantsev",
       description = """Check arrays""",
       ext_modules = [arr_check_module],
       py_modules = ["arr_check"],
       )
