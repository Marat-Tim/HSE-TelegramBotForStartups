import os
import pickle
from TaskClass import TaskClass

class DataBase:
    def __init__(self, name: str):
        self.path = name
        if not os.path.exists(f"data/{name}"):
            os.mkdir(f"data/{name}")

    def add(self, obj):
        with open(f"data/{self.path}/{obj.id}", 'w+') as f:
            pickle.dump(obj, f)

    def get_by_id(self, id):
        with open(f"data/{self.path}/{id}", 'rb') as f:
            return pickle.load(f)

    def update(self, obj):
        with open(f"data/{self.path}/{obj.id}", 'wb') as f:
            pickle.dump(obj, f)

def get_task_by_id(id: int) -> TaskClass:
    with open(f"data/tasks/{id}.task", 'rb') as f:
        return pickle.load(f)

def update_task(task: TaskClass):
    with open(f"data/tasks/{task.id}.task", 'wb') as f:
        pickle.dump(task, f)

