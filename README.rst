Notable
=======

About
-----

Python command-line utility to manage notes.

Installation
------------

*on most UNIX-like systems, you’ll probably need to run the following
``install`` commands as root or by using sudo*

**pip**

::

      pip install notable

**from source**

::

      pip notable git+http://github.com/goliatone/notable

*or*

::

      git clone git@github.com:goliatone/notable.git
      cd notable
      python setup.py install

as a result, the ``notable`` executable will be installed into a system
``bin`` directory

Roadmap
-------

-  TODO: Refactor and rewrite tests.
-  TODO: Use nosetests.
-  DONE: Add sphinx integration.
-  TODO: Let user update defaults, and save.
-  TODO: Use args for ``name`` and ``content`` instead.
-  TODO: Add ``vervose`` options.
-  DONE: Use config.
-  REVIEW: Rename config.ini to notable.conf (?)