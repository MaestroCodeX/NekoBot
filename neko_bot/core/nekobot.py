"""Nekobot Client"""

import logging
import signal

from pyrogram import asyncio, idle
from typing import Optional, Any, Awaitable, List

from neko_bot.config import Config
from .ext import pool, RawClient

LOGGER = logging.getLogger(__name__)


class NekoBot(RawClient):
    """NekoBot client"""

    def __init__(self, **kwargs):
        LOGGER.info("Setting up bot client...")
        kwargs = {
            "api_id" : Config.API_ID,
            "api_hash" : Config.API_HASH,
            "bot_token" : Config.BOT_TOKEN,
            "session_name" : ":memory:",
        }
        super().__init__(**kwargs)


    async def start(self):
        """ Start client """
        pool.start()
        LOGGER.info("Starting Bot Client...")
        await super().start()


    async def stop(self):
        """ Stop client """
        LOGGER.info("Exiting bot...")
        await super().stop()
        await pool.stop()

    def begin(self, coro: Optional[Awaitable[Any]] = None) -> None:
        """ Start RobOto """

        lock = asyncio.Lock()
        tasks: List[asyncio.Task] = []

        async def finalized() -> None:
            async with lock:
                for task in tasks:
                    task.cancel()
                if self.is_initialized:
                    await self.stop()
                [t.cancel() for t in asyncio.all_tasks() if t is not asyncio.current_task()]
                await self.loop.shutdown_asyncgens()
                self.loop.stop()
                LOGGER.info("Loop stopped")

        async def shutdown(sig: signal.Signals) -> None:
            LOGGER.info(f"Received Stop Signal [{sig.name}], Exiting...")
            await finalized()

        for sig in (signal.SIGHUP, signal.SIGTERM, signal.SIGINT):
            self.loop.add_signal_handler(
                sig, lambda sig=sig: self.loop.create_task(shutdown(sig)))

        self.loop.run_until_complete(self.start())

        try:
            if coro:
                LOGGER.info("Running Coroutine")
                self.loop.run_until_complete(coro)
            else:
                LOGGER.info("Idling")
                idle()
            self.loop.run_until_complete(finalized())
        except (asyncio.exceptions.CancelledError, RuntimeError):
            pass
        finally:
            self.loop.close()
            LOGGER.info("Loop closed")