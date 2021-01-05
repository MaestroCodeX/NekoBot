"""Module For Configuration NekoBot"""

from os import environ
from dotenv import load_dotenv


load_dotenv("config.env")




class Config:    # pylint: disable=too-few-public-methods
    """
    all config using python-dotenv
    """

    # pyrogram required
    BOT_TOKEN = environ.get("BOT_TOKEN")
    API_ID = int(environ.get("API_ID"))
    API_HASH = environ.get("API_HASH")
    # Staff  required
    OWNER_ID = int(environ.get("OWNER_ID"))
    # Optional
    SUDO_USERS = {int(x) for x in environ.get("SUDO_USERS", "").split()}
