"""Staff tools modules, just for staff."""

import datetime

from neko_bot.utils import staff
from neko_bot import neko, command


@neko.on_message(command("ping"))
@neko.send_action()
@staff()
async def pinger(_, message):
    """Pinger tools"""
    start = datetime.datetime.now()
    reply = await message.reply_text(f"`Pinging...`")
    finish = datetime.datetime.now()
    result = (finish - start).microseconds / 1000
    await reply.edit(f"**Pong!!!**\n`{result} ms`")

__MODULE__= "staff"
