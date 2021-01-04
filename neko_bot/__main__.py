"""Module main starter"""

import logging

from pyrogram import filters

from . import neko
from .core.logging import setup_log

LOGGER = logging.getLogger(__name__)


@neko.on_message(filters.command("start"))
async def start(bot, message):
    """This Start command."""
    getme = await neko.get_me()
    await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")
    LOGGER.info(neko)
    LOGGER.info(bot)


if __name__ == "__main__":
    setup_log()
    neko.begin()
