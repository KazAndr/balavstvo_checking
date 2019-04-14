#!/usr/bin/env python3

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


example_module = Extension('_PtrToStr',
                           sources=['PtrToStr_wrap.cxx', 'PtrToStr.cpp'],
                           )

setup (name = 'PtrToStr',
       version = '0.1',
       author      = "Kazantsev",
       description = """Конвертация указателя long double в строку""",
       ext_modules = [example_module],
       py_modules = ["PtrToStr"],
       )
