#! /usr/bin/python

import os
from setuptools import setup, find_packages

from notable import VERSION

description = "A command-line utility to manage Notes."

cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.md')).read()
except:
    long_description = description

setup(
    name="notable",
    version=VERSION,
    url='https://github.com/goliatone/notable',
    license='MIT',
    description=description,
    long_description=long_description,
    author='goliatone',
    author_email='hello@goliatone.com',
    packages=find_packages('notable',
                            exclude=['tests', 'experimental']),
    package_dir={'': 'notable'},
    install_requires=['setuptools', 'cement'],
    entry_points="""
    [console_scripts]
    notable = notable.cli.main:run
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    # test_suite='nose.collector',
)
