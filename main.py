from pyrogram import Client, filters
import config

bot = Client("my_account", bot_token=config.bot_token)


bot.run()