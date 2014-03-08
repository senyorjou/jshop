# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import src
version = src.__version__

setup(
    name='src',
    version=version,
    author='',
    author_email='smyslov@gmail.com',
    packages=[
        'src',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['src/manage.py'],
)