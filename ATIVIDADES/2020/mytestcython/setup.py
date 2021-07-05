#!/usr/bin/env python
# # -*- coding: UTF-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("cadastro_user.py"),)