
import os
import shutil
from cement.core import hook


def setup_config(app):
    print '>' * 60
    if not app.config.has_section('notario_user'):
        return

    # get user config file.
    abs_dir = app.config.get('notario_user', 'config')
    cnf_dir = os.path.dirname(abs_dir)

    if os.path.exists(abs_dir):
        return

    print 'IT SHOULD NEVER BE CALLED'
    # create abs_path
    if not os.path.exists(cnf_dir):
        os.makedirs(cnf_dir)

    f = file(abs_dir, "a+")
    f.close()

    dfl_dir = app.config.get('notario_user', 'default')

    shutil.copy2(dfl_dir, abs_dir)


def load():
    # hook.register('post_setup', setup_config)
    # hook.register('pre_close', cleanup)
    pass
