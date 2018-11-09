#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://jeopardy.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='jeopardy',
    version='0.0.1',
    description='Jeopardy utkML competition.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Todd Young',
    author_email='young.todd.mk@gmail.com',
    url='https://github.com/yngtodd/jeopardy',
    packages=[
        'jeopardy',
    ],
    package_dir={'jeopardy': 'jeopardy'},
    include_package_data=True,
    install_requires=[
        'tqdm'
    ],
    license='MIT',
    zip_safe=False,
    keywords='jeopardy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
