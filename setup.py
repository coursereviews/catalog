#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'catalog',
]

requires = [
    'requests>=2.7,<2.8',
    'xmltodict>=0.9,<0.10'
]

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='catalog',
    version='0.0.1',
    install_requires=requires,
)
