"""Module main starter"""

from . import neko
from .core.logging import setup_log


if __name__ == "__main__":
    setup_log()
    neko.begin()
