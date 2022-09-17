from TaskClass import TaskClass
from UserClass import User
from Session import Session
from datetime import datetime

def start_session(task: TaskClass, user: User) -> Session:
    session = Session(user.telegram_id, task.id, datetime.now())
    return session