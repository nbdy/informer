from requests import post
from json import dumps
from os import listdir



class Client(object):
    url = None

    def __init__(self, host="127.0.0.1", port=58008, ssl=False):
        if not ssl:
            self.url = "http://"
        else:
            self.url = "https://"
        self.url += (host + ":" + str(port)) + "/api/"

    def add(self, url, xpath, value, client_config):
        if not client_config["name"] in listdir("clients/"):
            return False


