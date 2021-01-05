"""Start modules.."""

import logging

from neko_bot import neko, command

__MODULE__ = "start"

LOGGER = logging.getLogger(__name__)


@neko.on_message(command("start"))
@neko.send_action()
async def start(_, message):
    """Start command."""
    getme = await neko.get_me()
    await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")
