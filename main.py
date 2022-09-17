from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import datetime

from DataBase import DataBase
import config

bd_users = DataBase("users")
bot = Client(config.bot_name, bot_token=config.bot_token)

import Start
import AddTask
import GetMyTasks
import GetAllTasks
# import GetTask

functions = {
    "start" : Start.start,
    "add_task" : AddTask.add_task,
    # "asign_task" :
    # "get_my_tasks" : GetMyTasks.get_my_tasks
    "get_all_tasks" : GetAllTasks.get_all_tasks
}

async def message_handler(message):
    if message.text[0] != "/":
        return False
    def convert(string):
        # if flag is true then until not symbol
        def read_from_index_until_symbol(index, symbol, flag=False):
            result = ""
            while index < len(string) and ((string[index] != symbol) ^ flag):
                result += string[index]
                index += 1
            return result, index

        result = []
        ind = 1
        var, ind = read_from_index_until_symbol(ind, " ")
        ind = read_from_index_until_symbol(ind, '"')[1] + 1
        result.append(var)
        while ind < len(string):
            var, ind = read_from_index_until_symbol(ind, '"')
            result.append(var)
            ind += 1
            ind = read_from_index_until_symbol(ind, '"')[1] + 1
        return result

    temp = convert(message.text)
    func = temp[0]
    temp = temp[1:]
    args = []
    match func:
        case "add_task":
            args = [temp[0], temp[1], datetime.datetime.strptime(temp[2], "%d.%m.%Y")]
        case "get_all_task":
            args = []
        case "start":
            args = []
    result = functions[func](*args)
    if result is not None:
        await bot.send_message(text=result, chat_id=config.chat_id)

@bot.on_message()
async def get_messages(client, message):
    await message_handler(message)

bot.run()