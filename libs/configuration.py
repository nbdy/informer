from sys import argv


class Configuration(object):
    headless = False
    driver = "chrome"
    executable_path = "chrome/linux/chromedriver"

    @staticmethod
    def help():
        print("usage: python3 Informer.py {arguments}")
        print("\t-h\t--help")
        print("\t-d\t--driver\tsets the webdriver")
        print("\t\tdefault: chrome")
        print("\t\tpossible arguments: chrome, c, firefox, f")
        print("\t-e\t--executable-path\tpath to driver")
        print("\t\tdefault:", Configuration.executable_path)
        print("\t--headless\trun browser headless")
        print("\t\tpossible arguments: none")
        exit()

    @staticmethod
    def parse():
        i = 0
        c = Configuration()
        while i < len(argv):
            a = argv[i]
            if a in ["-h", "--help"]:
                Configuration.help()
            elif a in ["-d", "--driver"]:
                c.driver = argv[i + 1]
            elif a in ["--headless"]:
                c.headless = True
            i += 1
        return c
