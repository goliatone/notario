#! /usr/bin/python

import os
from setuptools import setup, find_packages

version = '0.1.0'

description = "A command-line interface to the GitHub Issues API v2."
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.rst')).read()
except:
    long_description = description

setup(
    name="notable",
    version=version,
    url='https://github.com/goliatone/notable',
    license='MIT',
    description=description,
    long_description=long_description,
    author='goliatone',
    author_email='hello@goliatone.com',
    packages=find_packages('lib'),
    # package_dir={'': 'lib'},
    install_requires=['setuptools', 'cement'],
    entry_points="""
    [console_scripts]
    notable = notable:run
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
    test_suite='nose.collector',
)
