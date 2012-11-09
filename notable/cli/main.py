import os
import sys
from cement.core import foundation, backend
from cement.core import exc as cement_exc
from cement.utils import fs

# for some reason, we need this to find modules...?
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from notable.cli.controllers.base import NotableBaseController
from notable.core import exc as notable_exc

 # TODO: figure out if we want to have also a ~/notable.ini
file_path = os.path.abspath(__file__)
config_path = os.path.dirname(file_path) + '/config.ini'

defaults = backend.defaults('notable')
defaults['notable']['dir'] = os.path.expanduser('~') + "/.notes/"
defaults['notable']['ext'] = ".txt"
defaults['notable']['edt'] = "subl"


class NotableApp(foundation.CementApp):
    class Meta:
        label = 'notable'
        # bootstrap = 'notable.cli.bootstrap'
        base_controller = NotableBaseController
        # config_defaults = defaults

        # REVIEW: Should extension be .conf instead?
        config_files = [
            config_path,
            '/etc/notable/notable.ini',
            '~/.notable.ini',
            '~/.notable/config'
        ]

    def validate_config(self):
        # fix paths
        def_dir = self.config.get('notable', 'dir')
        print def_dir
        print os.path.expanduser('~') + "/.notes/"
        abs_dir = os.path.expanduser('~') + def_dir
        self.config.set('notable', 'dir', abs_dir)
        print "Abs path: %s" % abs_dir
        # create abs_path
        if not os.path.exists(abs_dir):
            os.makedirs(abs_dir)


def run():

    app = NotableApp()
    # app = NotableApp(config_files=[config_path])

    #handler
    try:
        app.setup()
        print app.config.get_sections()
        print app.config.options('notable')
        app.run()
    except notable_exc.NotableArgumentError as e:
        print("NotableArgumentError: %s" % e.msg)
    except cement_exc.CaughtSignal as e:
        print(e)
    except cement_exc.FrameworkError as e:
        print(e)
    finally:
        app.close()


def get_test_app(**kw):
    from tempfile import mkdtemp

    test_defaults = defaults
    test_defaults['notable']['data_dir'] = mkdtemp()
    kw['defaults'] = kw.get('defaults', defaults)
    kw['config_files'] = kw.get('config_files', [])
    kw['default_sources'] = kw.get('default_sources', None)

    app = NotableApp(**kw)
    return app

if __name__ == '__main__':
    run()
