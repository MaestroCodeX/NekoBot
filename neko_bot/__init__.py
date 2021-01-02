"""Initialize Framework"""

import logging
from .config import Config  # noqa: F401
from .nekobot import neko  # noqa: F401


# enable logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


logging.getLogger("pyrogram").setLevel(logging.WARNING)
