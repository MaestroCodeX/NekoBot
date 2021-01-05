"""Initialize Framework"""

from .core.nekobot import NekoBot
from .core.method import command
from .config import Config


neko = NekoBot()  # pylint: disable = C0103
