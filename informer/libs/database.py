import dataset


class DatabaseSiteObject(object):
    dbid = None
    url = None
    target_by = None
    target = None
    timeout = 10

    def __init__(self, **kwargs):
        kg = kwargs.get
        kk = kwargs.keys()
        if "obj" in kk:
            o = kg("obj")
            self.url = o.url
            self.target_by = o.target_by
            self.target = o.target
            self.timeout = o.timeout
        if "url" in kk:
            self.url = kg("url")
        if "target_by" in kk:
            self.target_by = kg("target_by")
        if "target" in kk:
            self.target = kg("target")
        if "timeout" in kk:
            self.timeout = kg("timeout")

    @staticmethod
    def from_site(obj):
        return DatabaseSiteObject(obj=obj)


class Database(object):
    db = None

    def __init__(self):
        self.db = dataset.connect("sqlite:///storage.db")

    def add_watcher(self, config):
        pass
