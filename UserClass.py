class User:
    def __init__(self, telegram_id="", telegram_handle="", name=""):
        self.telegram_id = telegram_id
        self.telegram_handle = telegram_handle
        self.name = name

    def id(self):
        return self.telegram_handle