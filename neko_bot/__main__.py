"""Module main starter"""

from neko_bot.core.decorators.admin_check import staff
from neko_bot.core.logging import LOGGER
from neko_bot import cust_cmd
from .nekobot import neko


@staff()
@neko.on_message(cust_cmd.command(commands=("start")))
async def start(_, message):
    """This Start command"""
    getme = await neko.get_me()
    LOGGER.debug("%s", getme)
    await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")
    LOGGER.info("Done")

if __name__ == "__main__":
    neko.run()
