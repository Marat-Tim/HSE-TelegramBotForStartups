import datetime
import os
from TaskClass import TaskClass
import pickle

def daily_result():
    after_dead = []
    for file in os.listdir("data/tasks"):
        with open(file, 'rb') as f:
            task: TaskClass = pickle.load(f)
            if (not task.is_ready and task.end < datetime.datetime.now()):
                after_dead.append(task)

    failed = f"Вы просрочили {len(after_dead)} задач: \n"
    for task in after_dead:
        failed += task.title + '\n'
    return failed