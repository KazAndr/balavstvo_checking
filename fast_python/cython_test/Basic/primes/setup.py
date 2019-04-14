from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['primes_cy.pyx',   # Cython code file with primes() function
                           'primes_py_cy.py', # Python code file with primes_python_compiled() function
                           'primes_cplus.pyx'], # Cython code file with std::vector 
                          annotate=True),        # enables generation of the html annotation file
)