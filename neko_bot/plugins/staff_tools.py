"""Staff tools modules, just for staff."""

import datetime
from typing import ClassVar

from neko_bot import neko, command
from neko_bot.utils import staff

__MODULE__ = "staff"


class Ping:  # pylint: disable = too-few-public-methods
    """Pinger tools"""
    name: ClassVar[str] = "Ping"

    @neko.on_message(command("ping"))
    @neko.send_action()
    @staff()
    async def cmd_ping(self, message):
        """Return bot ping in ms"""
        start = datetime.datetime.now()
        reply = await message.reply_text("`Pinging...`")
        finish = datetime.datetime.now()
        result = (finish - start).microseconds / 1000
        await reply.edit(f"**Pong!!!**\n`{result} ms`")
