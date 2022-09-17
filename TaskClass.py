import datetime
class TaskClass:
    def __init__(self, title, end=datetime.date(0, 0, 0), users=[], description=''):
        self.end = end
        self.users = users
        self.title = title
        self.description = description
