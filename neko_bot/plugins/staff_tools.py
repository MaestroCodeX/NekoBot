"""Staff tools modules, just for staff."""

import datetime

from neko_bot.utils import staff
from neko_bot import neko, command
from typing import ClassVar

__MODULE__ = "staff"


class Ping:
    """Pinger tools"""
    name: ClassVar[str] = "Ping"

    @neko.on_message(command("ping"))
    @neko.send_action()
    @staff()
    async def cmd_ping(self, message):
        start = datetime.datetime.now()
        reply = await message.reply_text("`Pinging...`")
        finish = datetime.datetime.now()
        result = (finish - start).microseconds / 1000
        await reply.edit(f"**Pong!!!**\n`{result} ms`")
