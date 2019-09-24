from . import Runnable
from flask import Flask, request, make_response
from json import dumps, loads


class API(Runnable):
    app = None

    def __init__(self, host="0.0.0.0", port=58008, debug=False, threaded=True):
        Runnable.__init__(self)
        self.app = Flask("API")
        self._init_app()
        self.app.run(host, port, debug, threaded=threaded)

    @staticmethod
    def get_json():
        data = request.get_data()
        try:
            return loads(data)
        except Exception as e:
            print(e)
        return None

    def _init_app(self):
        @self.app.route("/api/add", methods=["POST"])
        def add():
            data = self.get_json()

            return make_response(dumps({"ok": "?"}))

    def stop(self):
        f = request.environ.get("werkzeug.server.shutdown")
        if f is not None:
            f()
        self.do_run = False
