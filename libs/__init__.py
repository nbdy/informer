from threading import Thread
from os.path import dirname, basename, isfile, join
import glob

# https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


class Runnable(Thread):
    daemon = True
    do_run = False

    def __init__(self):
        Thread.__init__(self)
        self.do_run = True

    def _run(self):
        self.do_run = False

    def run(self):
        while self.do_run:
            self._run()

    def stop(self):
        self.do_run = False
