from UserClass import  User
from typing import List
from TaskClass import TaskClass
import pickle
import datetime

async def add_task(title: str, description: str, deadline: datetime.datetime):
    try:
        with open("data/temporary/add_task_last_id.txt", "rb") as f:
            last_id:int = pickle.load(f)
    except FileNotFoundError:
        last_id = 0
    Task = TaskClass(last_id, title, deadline, [], description)
    with open(f"data/tasks/{last_id}.task", "wb") as f:
        pickle.dump(Task, f)
    last_id += 1
    with open("data/temporary/add_task_last_id.txt", "wb") as f:
        pickle.dump(last_id, f)
    return "Successfully add task"

