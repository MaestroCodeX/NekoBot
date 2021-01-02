"""Module For Configuration NekoBot"""
import os
from dotenv import load_dotenv


load_dotenv("config.env")


class Config: # pylint: disable=too-few-public-methods
    """
    all config using python-dotenv
    """

    # pyrogram required
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    # Staff  required
    OWNER_ID = os.environ.get("OWNER_ID")
    SUDO_USERS = os.environ.get("SUDO_USERS")
    # Optional
