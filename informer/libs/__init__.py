from threading import Thread


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


class WatcherConfiguration(object):
    every = 10 * 1000 * 60  # every hour
    site = None
    endpoint = None

    def __init__(self, **kwargs):
        if "every" in kwargs.keys():
            self.every = kwargs.get("every")
        if "site" in kwargs.keys():
            self.site = kwargs.get("site")
        if "endpoint" in kwargs.keys():
            self.endpoint = kwargs.get("endpoint")


class Watcher(object):
    def __init__(self):
        pass

    @staticmethod
    def from_cfg(cfg):
        return Watcher()
