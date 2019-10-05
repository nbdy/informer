#!/usr/bin/python3

from seleniumwrapper.configuration import Configuration
from seleniumwrapper.webdriver import WebDriver
from seleniumwrapper import fetch as fetch_webdriver
from libs.api import API


class InfoSite(object):
    site = None
    info_endpoint = None

    def __init__(self, site, info_endpoint):
        self.site = site()
        self.info_endpoint = info_endpoint

    def check(self):
        pass


class Informer(object):
    info_sites = []
    sleep_time = 60 * 60  # every hour

    api = None
    config = None

    def __init__(self, config):
        self.api = API()
        self.config = config
        self.driver = WebDriver.build(config)

    def stop(self):
        self.api.stop()


if __name__ == '__main__':
    fetch_webdriver()
    c = Configuration.parse()
    # c.headless = True
    i = Informer(c)
