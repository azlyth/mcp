#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='mcp',
    version='1.0',
    description='Watch over your systems',
    author='Peter Valdez',
    author_email='ptr.vldz@gmail.com',
    packages=['mcp'],
    entry_points={
        'console_scripts': [
            'mcp = mcp.__main__:main'
        ]
    }
)
