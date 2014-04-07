# -*- coding: utf-8 -*-
import os
import sys
import shutil

__version__ = '0.7.0'
__version_info__ = tuple([int(num) for num in __version__.split('.')])

# VERSION = (0, 0, 1, 'dev')

MINIONS_PATH = '~/.notario'

# __version__ = '.'.join((str(each) for each in VERSION[:4]))

__author__ = 'goliatone'


def get_version():
    return __version__
    # return '.'.join((str(each) for each in VERSION[:3]))


def get_minion_path(minion=None):
    if not minion:
        return os.path.expanduser(MINIONS_PATH)
    return os.path.join(get_minion_path(), minion)


#TODO: This will break, need to use setup tools.
def install_minion_config(minion=None, config='config', template=None):
    if not os.path.isdir(get_minion_path()):
        os.mkdir(get_minion_path())

    filename = get_minion_path(config)
    if not os.path.isfile(filename):
        try:
            shutil.copy2(template, filename)
        except:
            print "Unable to install configuration file"
            sys.exit()
