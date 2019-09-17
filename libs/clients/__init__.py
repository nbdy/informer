

class Client(object):
    target = None

    def __init__(self, target):
        self.target = target

    def inform(self, msg):
        print(self.target, "not informing anything", msg)
