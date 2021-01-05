"""Initialize Framework"""
import logging
from .core.nekobot import NekoBot
from .config import Config

LOGGER = logging.getLogger(__name__)

neko = NekoBot()
