import os
import logging
import colorlog


def setup_log():
    """Configures logging"""
    level = logging.INFO
    file_path = 'neko_bot/core/logging/NekoBot.log'

    if os.path.exists(file_path):
        os.remove(file_path)

    # Logging into file
    format = "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"
    logfile = logging.FileHandler(file_path)
    formatter = logging.Formatter(format, datefmt="%H:%M:%S")
    logfile.setFormatter(formatter)
    logfile.setLevel(level)

    # Logging into stdout with color
    format = ("%(bold)s%(asctime)s%(reset)s: "
              "%(log_color)s%(levelname)s%(reset)s - %(name)s - "
              "%(log_color)s%(message)s%(reset)s")
    stream = logging.StreamHandler()
    formatter = colorlog.ColoredFormatter(format, datefmt="%H:%M:%S")
    stream.setLevel(level)
    stream.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)
    root.addHandler(logfile)
    root.addHandler(stream)

    logging.getLogger("pyrogram").setLevel(logging.WARNING)
