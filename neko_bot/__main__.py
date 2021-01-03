"""Module main starter"""

import asyncio

from pyrogram import idle
from pyrogram import filters

from neko_bot.core.decorators import staff
from neko_bot.core.decorators import chat_action
from .nekobot import neko


async def bot_startup():
    """Bot startup."""
    await neko.start()
    await idle()


@neko.on_message(filters.command("start"))
@staff()
@chat_action()
async def start(_, message):
    """This Start command."""
    getme = await neko.get_me()
    await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")


if __name__ == "__main__":
    task = asyncio.get_event_loop()
    task.run_until_complete(bot_startup())
