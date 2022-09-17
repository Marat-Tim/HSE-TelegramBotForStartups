import datetime
import json

class TaskClass:
    def __init__(self, id: int, title: str, end=datetime.datetime(2000, 1, 1), users=None, description='', is_ready=False):
        self.id = id
        self.end = end
        self.users = users
        self.title = title
        self.description = description
        self.is_ready = is_ready

    def __str__(self):
        return json.dumps(self)

