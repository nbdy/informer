

class WebDriver(object):
    FIREFOX_DRIVER_NAMES = ["f", "firefox"]
    CHROME_DRIVER_NAMES = ["c", "chrome"]

    @staticmethod
    def build(cfg):
        d = None
        o = None
        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            from selenium.webdriver import Firefox
            from selenium.webdriver.firefox.options import Options
            d = Firefox
            o = Options()
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            from selenium.webdriver import Chrome
            from selenium.webdriver.chrome.options import Options
            d = Chrome
            o = Options()

        o.headless = cfg.headless
        return d(cfg.executable_path, options=o)
