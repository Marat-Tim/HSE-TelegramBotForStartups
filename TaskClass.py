import datetime

class TaskClass:
    def __init__(self, title: str, end=datetime.date(0, 0, 0), users=None, description=''):
        self.end = end
        self.users = users
        self.title = title
        self.description = description
