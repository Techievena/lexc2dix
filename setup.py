#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages, setup
from lexc2dix import release

os.listdir(os.path.join('lexc2dix'))

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python3 setup.py install\'')
    print()

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()
with open('test-requirements.txt') as requirements:
    test_required = requirements.read().splitlines()
with open("README.md") as readme:
    long_description = readme.read()

if __name__ == "__main__":
    setup(
        name=release.name,
        version=release.__version__,
        author=release.__author__,
        author_email=release.__email__,
        description=release.__description__,
        url=release.__url__,
        download_url=release.__download_url__,
        keywords=['lexc', 'twolc', 'monodix', 'Apertium', 'HFST'],
        packages=find_packages(exclude=["build.*", "tests", "tests.*"]),
        install_requires=required,
        tests_require=test_required,
        long_description=long_description,
        scripts=['api/lexc2dix_api.py'],
        license='GNU GENERAL PUBLIC LICENSE',
        entry_points={
            'console_scripts': [
                'lexc2dix = lexc2dix_api:main'
            ]
        },
        python_requires='>=3',
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ],
    )
