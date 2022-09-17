import pickle
from TaskClass import TaskClass

def get_task_by_id(id: int) -> TaskClass:
    with open(f"data/tasks/{id}.task", 'rb') as f:
        return pickle.load(f)

def update_task(task: TaskClass):
    with open(f"data/tasks/{task.id}.task", 'wb') as f:
        pickle.dump(task, f)

