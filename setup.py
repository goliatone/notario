#! /usr/bin/python

import os
import glob
from setuptools import setup, find_packages

from notable import VERSION

description = "A command-line utility to manage notes."

cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README')).read()
except:
    long_description = description

datadir = os.path.join(cur_dir, 'data', 'config')
datafiles = [(datadir, [f for f in glob.glob(os.path.join(datadir, '*'))])]
print '*' * 20
print datafiles
print '*' * 20
setup(
    name="notable",
    version=VERSION,
    description=description,
    long_description=long_description,
    url='https://github.com/goliatone/notable',
    license='MIT',
    author='goliatone',
    author_email='hello@goliatone.com',
    keywords='command-line utils notes',
    packages=find_packages('notable',
                            exclude=['experimental']),
                            # exclude=['tests', 'experimental']),
    package_dir={'': 'notable'},
    # package_data={'': ['config.ini']},
    data_files=datafiles,
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
    test_suite='tests'
)
