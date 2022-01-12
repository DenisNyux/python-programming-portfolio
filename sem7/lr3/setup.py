from setuptools import setup
from Cython.Build import cythonize

setup(
    name='integrate_fnc',
    ext_modules=cythonize("c_integrate.pyx"),
    zip_safe=False,
)
