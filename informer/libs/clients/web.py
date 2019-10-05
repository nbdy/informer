from . import Client
import requests


class WebClient(Client):
    def inform(self, msg):
        requests.post(self.target, msg)
