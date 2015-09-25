#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'catalog'
]

requires = [
    'requests>=2.7,<2.8',
    'xmltodict>=0.9,<0.10',
    'six>=1.9,<2.0'
]

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='catalog',
    version='0.0.1',
    url='https://github.com/coursereviews/catalog',
    author='Dana Silver',
    author_email='dsilver@middlebury.edu',
    install_requires=requires,
    packages=packages,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    )
)
