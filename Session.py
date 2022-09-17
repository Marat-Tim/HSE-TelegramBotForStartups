import datetime

class Session:

    def __init__(self, user_id: int, task_id: int, begin: datetime.datetime, end=datetime.datetime(2000, 1, 1)):
        self.user_id = user_id
        self.task_id = task_id
        self.begin = begin
        self.end = end