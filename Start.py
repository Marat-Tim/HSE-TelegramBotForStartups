import config
from UserClass import User

async def start(bot, bd_users):
    async for member in bot.get_chat_members(config.chat_id):
        if member.user.is_bot():
            continue
        bd_users.add(User(member.user.id, member.user.username, member.user.last_name + " " + member.user.first_name))
    return "Initialization finished successfully."