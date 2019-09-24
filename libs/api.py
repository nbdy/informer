from . import Runnable
from flask import Flask, request, make_response
from json import dumps, loads
from os import listdir, getcwd
from os.path import abspath


class API(Runnable):
    app = None

    callback_add = None

    def __init__(self, host="0.0.0.0", port=58008, debug=False, threaded=True, callback_add=None):
        Runnable.__init__(self)
        self.app = Flask("API")
        self._init_app()
        self.callback_add = callback_add
        self.app.run(host, port, debug, threaded=threaded)

    @staticmethod
    def get_json():
        data = request.get_data()
        try:
            return loads(data)
        except Exception as e:
            print(e)
        return None

    @staticmethod
    def check_dict(d, keys):
        for k in keys:
            if k not in d.keys():
                return False
        return True

    @staticmethod
    def get_current_path():
        return abspath(getcwd()) + "/"

    def set_callback_add(self, callback):
        pass

    def add(self, data):
        if data is None or not self.check_dict(data, ["name", "config"]):
            return False

        return True

    def _init_app(self):
        @self.app.route("/api/add", methods=["POST"])
        def add():
            return make_response(dumps({"error": self.add(self.get_json())}))

    def stop(self):
        f = request.environ.get("werkzeug.server.shutdown")
        if f is not None:
            f()
        self.do_run = False
