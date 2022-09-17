import datetime
import json

class TaskClass:
    def __init__(self, id: int, title: str, end=datetime.datetime(2000, 1, 1), users=None, description='', is_ready=False, complete_time=datetime.datetime(2000, 1, 1)):
        self.id = id
        self.end = end
        self.users = users
        self.title = title
        self.description = description
        self.is_ready = is_ready
        self.complete_time = complete_time

    def __str__(self):
        return f"{{" \
               f"   id: {self.id}\n" \
               f"   title: {self.title}\n" \
               f"   end: {str(self.end)}\n" \
               f"   users: {self.users}\n" \
               f"   description: {self.description}\n" \
               f"   is ready: {self.is_ready}\n" \
               f"}}"

