"""Module main starter"""

from pyrogram import filters

from .nekobot import neko
from neko_bot.core.logging import LOGGER
from neko_bot.core.decorators.admin_check import staff

@staff()
@neko.on_message(filters.command("start"))
async def start(neko, message):
    getme = await neko.get_me()
    LOGGER.debug("%s", getme)
    await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")
    LOGGER.info("Done")

if __name__ == "__main__":
    neko.run()