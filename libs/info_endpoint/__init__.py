import ssl


class Client(object):
    ssl = None

    def __init__(self):
        ssl.create_default_context()

    def send(self, msg, target):
        print("not sending anything", msg)
