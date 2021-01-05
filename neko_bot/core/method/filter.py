import re
import shlex

from pyrogram.filters import create
from pyrogram.types import Message
from typing import Union, List


def command(commands: Union[str, List[str]],
            prefixes: Union[str, List[str]] = "/",
            case_sensitive: bool = False):

    async def func(flt, _, message: Message):
        text: str = message.text or message.caption
        message.command = []

        if not text:
            return False

        regex = "^({prefix})+\\b({regex})\\b(\\b@{bot_name}\\b)?(.*)".format(
            prefix="|".join(re.escape(x) for x in prefixes),
            regex="|".join(flt.commands).lower(),
            bot_name="NekoID_bot",
        )

        matches = re.search(re.compile(regex), text.lower())
        if matches:
            for arg in shlex.split(matches.group(4).strip()):
                if arg.startswith("@") and arg != "@nekoid_bot":
                    return False
                message.command.append(arg)
            return True
        return False

    commands = commands if type(commands) is list else [commands]
    commands = {c if case_sensitive else c.lower() for c in commands}

    prefixes = [] if prefixes is None else prefixes
    prefixes = prefixes if type(prefixes) is list else [prefixes]
    prefixes = set(prefixes) if prefixes else {""}

    return create(
        func,
        "CustomCommandFilter",
        commands=commands,
        prefixes=prefixes,
        case_sensitive=case_sensitive
    )
