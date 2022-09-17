from UserClass import User
from TaskClass import TaskClass
import DataBase

def addTaskToUser(id_task: int, current_user: User):
    current_task = DataBase.get_task_by_id(id_task)
    current_task.users.append(User)
    DataBase.update_task(current_task)

def deleteUserFromTask(id_task: int, current_user: User):
    current_task = DataBase.get_task_by_id(id_task)
    current_task.users.remove(User)
    DataBase.update_task(current_task)