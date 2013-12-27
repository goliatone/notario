Notario
=======

About
-----

Python command-line utility to manage notes.

Installation
------------

*on most UNIX-like systems, you’ll probably need to run the following*
``install`` *commands as root or by using sudo*

**pip**

::

      pip install Notario.minion

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
-  TODO: Add documentation.
-  *DONE: Add sphinx integration.*
-  *DONE: Let user update defaults, and save.*
-  TODO: Use args for ``name`` and ``content`` instead.
-  TODO: Add ``vervose`` options.
-  TODO: Add create from template.
-  *DONE: Use config.*
-  TODO: Integration with services.
-  *DONE: Rename config.ini to notario.conf (?)*


TODO:
Update how we handle input
ntr => should list
ntr <note_name> => should open it if exists, or should create it and open it
ntr <note_name> --delete/-d => should 'delete' it- move it to deleted dir.
ntr <note_name> -a "this text should get appended, last line"

http://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments?rq=1
http://stackoverflow.com/questions/13875173/python-argparse-nargs-and-optional-arguments?rq=1
http://stackoverflow.com/questions/15583870/mixing-positional-and-optional-arguments-in-argparse
