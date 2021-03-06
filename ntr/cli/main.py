import os
import sys
from cement.core import foundation, backend
from cement.core import exc as cement_exc
# from cement.utils import fs

# for some reason, we need this to find modules...?
module_path = os.path.join(os.path.dirname(__file__), '../..')
sys.path.append(module_path)

from ntr.cli.controllers.base import NotarioBaseController
from ntr.core import exc as ntr_exc

# Ugly, but how to improve?
USER_PATH = os.path.expanduser('~')
USER_PATH_CONFIG = USER_PATH + '/.notario/config'

 # TODO: figure out if we want to have also a ~/notario.ini
file_path = os.path.abspath(__file__)
base_path = os.path.dirname(file_path)
config_path = os.path.join(module_path, 'data/config/notario.cfg')

# Default values for the config.
defaults = backend.defaults('notario')
defaults['notario']['dir'] = "/.notes/"
defaults['notario']['ext'] = ".txt"
defaults['notario']['edt'] = "subl"

"""
Entry point for the Notario.minion application.
"""


class NotarioApp(foundation.CementApp):
    class Meta:
        label = 'notario'
        bootstrap = 'ntr.cli.bootstrap'
        base_controller = NotarioBaseController

        # Setup the default user config file location.
        if not 'notario_user' in defaults:
            defaults['notario_user'] = dict()

        defaults['notario_user']['config'] = USER_PATH_CONFIG
        defaults['notario_user']['default'] = config_path
        config_defaults = defaults

        # REVIEW: Should extension be .conf instead?
        # Updated order so that default loads last.
        config_files = [
            config_path,
            USER_PATH_CONFIG,
        ]

    def validate_config(self):
        """
        """
        # fix paths
        def_dir = self.config.get('notario', 'dir')
        abs_dir = USER_PATH + def_dir
        self.config.set('notario', 'dir', abs_dir)

        # create abs_path
        if not os.path.exists(abs_dir):
            os.makedirs(abs_dir)


def run():

    app = NotarioApp()
    # app = NotarioApp(config_files=[config_path])

    #handler
    try:
        app.setup()
        app.run()
    except ntr_exc.NotarioArgumentError as e:
        print("NotarioArgumentError: %s" % e.msg)
    except cement_exc.CaughtSignal as e:
        print(e)
    except cement_exc.FrameworkError as e:
        print(e)
    finally:
        app.close()


def get_test_app(**kw):
    from tempfile import mkdtemp

    test_defaults = defaults
    test_defaults['notario']['data_dir'] = mkdtemp()
    kw['defaults'] = kw.get('defaults', defaults)
    kw['config_files'] = kw.get('config_files', [])
    kw['default_sources'] = kw.get('default_sources', None)

    app = NotarioApp(**kw)
    return app

if __name__ == '__main__':
    run()
