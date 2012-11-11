Notario
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

      pip install notario

**from source**

::

      pip notario git+http://github.com/goliatone/notario

*or*

::

      git clone git@github.com:goliatone/notario.git
      cd notario
      python setup.py install

as a result, the ``notario`` executable will be installed into a system
``bin`` directory

Roadmap
-------

-  TODO: Refactor and rewrite tests.
-  TODO: Use nosetests.
-  DONE: Add sphinx integration.
-  TODO: Let user update defaults, and save.
-  TODO: Use args for ``name`` and ``content`` instead.
-  TODO: Add ``vervose`` options.
-  TODO: Add create from template.
-  DONE: Use config.
-  TODO: Integration with services.
-  REVIEW: Rename config.ini to notario.conf (?)