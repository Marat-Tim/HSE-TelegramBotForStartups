import pickle
from TaskClass import TaskClass

def get_task_by_id(id: int) -> TaskClass:
    with open(f"data/tasks/{id}.task", 'rb') as f:
        return pickle.load(f)


