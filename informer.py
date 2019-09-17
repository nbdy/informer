from threading import Thread

from libs.clients.web import WebClient
from libs.amazon import BoxFreshSpencerBrown46
from libs.configuration import Configuration
from libs.webdriver import WebDriver


class InfoSite(object):
    site = None
    info_endpoint = None

    def __init__(self, site, info_endpoint):
        self.site = site()
        self.info_endpoint = info_endpoint

    def check(self):
        pass


class Informer(Thread):
    do_run = True
    daemon = True
    info_sites = []
    sleep_time = 60 * 60  # every hour

    def __init__(self, driver, info_sites=[]):
        Thread.__init__(self)
        self.info_sites = info_sites

    def run(self):
        while self.do_run:
            for site in self.info_sites:
                print(site.check())

    def stop(self):
        self.do_run = False


if __name__ == '__main__':
    c = Configuration.parse()
    # c.headless = True
    d = WebDriver.build(c)
    i = Informer(d)
    i.info_sites.append(InfoSite(BoxFreshSpencerBrown46, WebClient("https://target.site/boop")))
    try:
        i.run()
    except KeyboardInterrupt:
        i.stop()
