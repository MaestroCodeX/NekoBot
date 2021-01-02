"""Nekobot Client"""

from pyrogram import Client
from . import Config

neko = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)
