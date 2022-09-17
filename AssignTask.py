from UserClass import User
from TaskClass import TaskClass
import DataBase

async def addTaskToUser(id_task: int, current_user: User):
    current_task = DataBase.get_task_by_id(id_task)
    current_task.users.append(current_user)
    DataBase.update_task(current_task)

async def deleteUserFromTask(id_task: int, current_user: User):
    current_task = DataBase.get_task_by_id(id_task)
    current_task.users.remove(current_user)
    DataBase.update_task(current_task)