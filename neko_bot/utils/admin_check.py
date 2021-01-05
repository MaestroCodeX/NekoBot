"""Decorators for user check."""
import logging
from functools import wraps
from typing import Optional

from neko_bot import Config

LOGGER = logging.getLogger(__name__)


async def adminlist(client, chat_id):
    """This Function to get admin list."""
    members = client.iter_chat_members(chat_id, filter="administrators")
    return [i.user.id for i in members]


def admin(coro):
    """This function build decorator for administ."""
    @wraps(coro)
    async def decorator(client, message, *args, **kwargs):
        chat_id = message.chat.id
        administ = await adminlist(client, chat_id, *args, **kwargs)
        if message.from_user.id in administ:
            return await coro(client, message, *args, **kwargs)
        else:
            return await message.reply_text("You are not an admin!")

    return decorator


def staff(rank: Optional[str] = "sudo"):
    """This Function for staff commands.

    Parameters:
        rank (str, default="sudo"): rank needed to trigger a command
    """

    def decorators(coro):

        @wraps(coro)
        async def check(client, message, *args, **kwargs):
            user_id = message.from_user.id
            if rank in ["owner", "sudo"] and user_id == Config.OWNER_ID:
                return await coro(client, message, *args, **kwargs)
            elif rank == "sudo" and user_id in Config.SUDO_USERS:
                return await coro(client, message, *args, **kwargs)
            else:
                LOGGER.warning("Unkown rank \"%s\"", rank)
                return
                

        return check

    return decorators
