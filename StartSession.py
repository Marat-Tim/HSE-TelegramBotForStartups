import pickle

from TaskClass import TaskClass
from UserClass import User
from Session import Session
from datetime import datetime

def start_session(task: TaskClass, user: User):
    now = datetime.now()
    session = Session(user.telegram_id, task.id, datetime.now())
    with open(f"{user.telegram_handle} {now}", 'wb') as f:
        pickle.dump(session, f)