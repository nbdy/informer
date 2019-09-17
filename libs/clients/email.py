from . import Client

import smtplib, ssl


class EmailClient(Client):
    host = None
    port = None
    username = None
    password = None
    sender = "info@me.io"

    template = """
    Subject: %s
    
    This message is sent from %s.
    """

    def __init__(self, host, username, password, port=25):
        Client.__init__(self)
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send(self, msg, target):
        with smtplib.SMTP_SSL(self.host, self.port, context=self.ssl) as s:
            s.login(self.username, self.password)
            s.sendmail(self.sender, target, msg)
