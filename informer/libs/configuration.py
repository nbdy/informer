from sys import argv
import json
from seleniumwrapper import Configuration as DriverConfiguration


class Configuration(object):
    _web_driver = None
    _site_configs = []

    @staticmethod
    def help():
        print("usage: ./informer.py {arguments}")
        print("\t{arguments}\t\t\t\t\t{info}")

        def chk(key):
            return not key.startswith("_") and key not in ["help", "parse", "UnexpectedArgumentException"]

        print("\t-sc", "\t--site-config", "\t\tcan be used more than once")

        for k in Configuration.__dict__.keys():
            if chk(k):
                print(k)
        for k in DriverConfiguration.__dict__.keys():
            if chk(k):
                print("\t-" + k[0], "\t\t--" + k)

        exit()

    @staticmethod
    def parse():
        i = 0
        cfg = Configuration()
        cfg._web_driver = DriverConfiguration.parse()
        while i < len(argv):
            a = argv[i]
            if a in ["-h", "--help"]:
                help()
            elif a in ["-sc", "--site-config"]:
                cfg._site_configs += json.load(open(argv[i + 1]))
            i += 1
        return cfg


if __name__ == '__main__':
    Configuration.help()
