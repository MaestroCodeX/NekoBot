"""Module main starter"""

import asyncio

from pyrogram import idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from neko_bot import cust_cmd
from neko_bot.core.decorators import chat_action, staff
from .nekobot import neko


async def bot_startup():
    """Bot startup."""
    await neko.start()
    await idle()


@neko.on_message(cust_cmd.command(commands=("start")))
@staff()
@chat_action()
async def start(_, message):
    """This Start command."""
    getme = await neko.get_me()
    await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")


if __name__ == "__main__":
    task = asyncio.get_event_loop()
    task.run_until_complete(bot_startup())
