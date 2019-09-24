from requests import post
from json import dumps



class Client(object):
    url = None

    def __init__(self, host="127.0.0.1", port=58008, ssl=False):
        if not ssl:
            self.url = "http://"
        else:
            self.url = "https://"
        self.url += (host + ":" + str(port)) + "/api/"

    def add(self, url, exists, endpoint):
        if endpoint in
