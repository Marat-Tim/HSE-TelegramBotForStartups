import pickle
import os
from TaskClass import TaskClass
def get_my_tasks(user_id: int):
    tasks = []
    for file in os.listdir("data/tasks"):
        with open(file, 'wb') as f:
            task:TaskClass = pickle.load(f)
            if (user_id in task.users):
                tasks.append(task)
    return tasks


