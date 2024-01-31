#!/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [Extension(
    'fish2pano.fast',
    ['fish2pano/fast.py'],
    include_dirs=[numpy.get_include()],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp']
)]

setup(
    name='fish2pano',
    ext_modules=cythonize(extensions)
)
