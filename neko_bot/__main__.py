"""Module main starter"""

import asyncio
from neko_bot import neko


async def start_neko():
    """Let's make bot starter"""
    await neko.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_neko())
