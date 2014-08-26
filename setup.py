#!/usr/bin/env python
from distutils.core import setup

setup(
    name='WixInstance',
    version='1.0.0',
    author='Jeffrey Chan',
    packages=['wixinstance'],
    url='https://github.com/jeffreychan637/wix-instance',
    license='MIT',
    description='This package is used to parse the Wix Instance in the backend'
                ' of a Wix application.',
    long_description=open('README.rst').read(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable'
    ]
)