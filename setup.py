#!/bin/env python
from Cython.Distutils import build_ext
from distutils.core import setup, Extension
import numpy
from Cython.Build import cythonize

setup(name='fish2pano',
      version='1.1.0',
      description='Converts an fisheye lens to panoramic',
      author='Russell Valentine',
      author_email="russ@coldstonelabs.org",
      url="http://coldstonelabs.org",
      py_modules=["fish2pano", "generate_pano", "findcircle.py"],
      ext_modules=[
          Extension(
              'generate_pano',
              ['generate_pano.py'],
              include_dirs=[numpy.get_include()],
              extra_compile_args=['-fopenmp'],
              extra_link_args=['-fopenmp']
          )
      ],
      )
