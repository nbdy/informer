from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from os.path import dirname, basename, isfile, join
import glob
sites = glob.glob(join(dirname(__file__), "*.py"))
sites = [basename(f)[:-3] for f in sites if isfile(f) and not f.endswith('__init__.py')]


class SiteObject(object):
    driver = None
    url = None
    target_by = By.ID
    target = None
    timeout = 10

    _element = None

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        if self.target is None:
            print("target is None; not waiting")
        else:
            try:
                return WebDriverWait(self.driver, self.timeout).until(expected_conditions.presence_of_element_located(
                    (self.target_by, self.target)))
            except TimeoutException as e:
                print(e.msg)
                print(e.stacktrace)
                return None

    def get(self):
        self.driver.get(self.url)
        self._element = self.wait()
        return self

    @staticmethod
    def build(driver, cfg):
        pass
