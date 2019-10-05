#!/usr/bin/python3

from seleniumwrapper.configuration import Configuration
from seleniumwrapper.webdriver import WebDriver
from seleniumwrapper import fetch as fetch_webdriver

from libs.sites import sites
from libs.api import API
from libs import Runnable


class Informer(Runnable):
    info_sites = []
    sleep_time = 60 * 60  # every hour

    db = None
    api = None
    config = None

    def __init__(self, config):
        Runnable.__init__(self)
        self.api = API(callback_add=self.callback_add_info_site)
        self.config = config
        self.driver = WebDriver.build(config)

    def callback_add_info_site(self, config):

        self.info_sites.append(config)  # todo filter if not already in list
        return True

    def _run(self):
        for i in self.info_sites:
            i.check()

    def stop(self):
        self.api.stop()


if __name__ == '__main__':
    fetch_webdriver()
    c = Configuration.parse()
    c.headless = True
    Informer(c).run()
