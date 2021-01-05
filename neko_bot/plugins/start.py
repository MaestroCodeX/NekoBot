from neko_bot import neko
from pyrogram import filters
from neko_bot import LOGGER


__MODULE__ = "start"


@neko.on_message(filters.command("start"))
async def start(bot, message):
    """This Start command."""
    getme = await neko.get_me()
    await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")
    LOGGER.info(neko)
    LOGGER.info(bot)
