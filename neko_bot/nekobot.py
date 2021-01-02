"""Nekobot Client"""

from pyrogram import Client
from neko_bot import Config, logging

LOGGER = logging.getLogger(__name__)

neko = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

LOGGER.info("Neko_bot initialized!")