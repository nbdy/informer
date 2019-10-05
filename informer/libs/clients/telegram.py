from . import Client
from telegram.ext import Updater, CommandHandler


class TelegramClient(Client):
    updater = None

    def __init__(self, token):
        Client.__init__(self, None)
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler("available", self.cmd_available))
        self.updater.dispatcher.add_handler(CommandHandler("new", self.cmd_new))
        self.updater.dispatcher.add_handler(CommandHandler("help", self.cmd_help))
        self.updater.dispatcher.add_error_handler()
        self.updater.start_polling()
        self.updater.idle()

    def error_hander(self, u, c):
        print(u, "caused", c.error)

    def cmd_available(self, u, c):
        u.message.reply_text("none")

    def cmd_new(self, u, c):
        u.message.reply_text("nothing")

    def cmd_help(self, u, c):
        txt = """help:\n
        /available\tshow available products\n
        /new\tshow products which were unavailable\n
        /help\tthis
        """
        u.message.reply_text(txt)

    def inform(self, msg):
        pass
