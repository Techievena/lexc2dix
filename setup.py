#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

os.listdir(os.path.join('lexc2dict'))

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

from lexc2dix import release

if __name__ == "__main__":
    setup(
        name = release.name,
        version = release.__version__,
        author = release.__author__,
        author_email = release.__email__,
        description = release.__description__,
        url = release.__url__,
        download_url = release.__download_url__,
        keywords= ['lexc', 'twolc', 'monodix'],
        packages = ['lexc2dix'],
        scripts = ['bin/lexc2dix_api'],
        license = 'GNU GENERAL PUBLIC LICENSE',
        entry_points = {
            'console_scripts': [
            'lexc2dix = lexc2dix_api:main'
            ]
        },
        install_requires = ['nose'],
        test_suite = 'nose.collector',
        tests_require = ['nose>=0.10.1']
    )