"""Start modules.."""

import logging

from neko_bot import neko, command
from typing import ClassVar

__MODULE__ = "start"

LOGGER = logging.getLogger(__name__)


class Start:
    """Start command"""
    name: ClassVar[str] = "Start"

    @neko.on_message(command("start"))
    @neko.send_action()
    async def cmd_start(self, message):
        getme = await neko.get_me()
        await message.reply_text(f"I'm alive\nMy name is {getme.first_name}")
