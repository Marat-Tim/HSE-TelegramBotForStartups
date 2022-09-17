import os
from TaskClass import TaskClass
import pickle

def get_all_tasks() -> str:
    text = ""
    for file in os.listdir("data/tasks"):
        with open(file, 'rb') as f:
            text += f"{str(pickle.load(f))}\n"
    return text

