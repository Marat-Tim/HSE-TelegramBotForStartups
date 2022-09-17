from pyrogram import enums
import config
from UserClass import User

def start():
    global bot, bd_users
    for member in bot.get_chat_members():
        if member.user.is_bot():
            continue
        bd_users.add(User(member.user.id, member.user.username, member.user.last_name + " " + member.user.first_name))