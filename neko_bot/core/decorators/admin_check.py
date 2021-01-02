"""Decorators for user check."""
from functools import wraps

from neko_bot import Config
from neko_bot.core.logging import LOGGER


async def adminlist(client, chat_id):
    """This Function to get admin list."""
    members = client.iter_chat_members(chat_id, filter="administrators")
    _admin = []
    async for i in members:
        _admin.append(i.user.id)
    return _admin


def admin(coro):
    """This function build decorator for administ."""
    @wraps(coro)
    async def decorator(client, message):
        chat_id = message.chat.id
        administ = await adminlist(client, chat_id)
        if message.from_user.id in administ:
            return await coro(client, message)
        else:
            return await message.reply_text("You are not an admin!")

    return decorator


def staff(rank: str = "sudo"):
    """This Function for staff commands.

    Parameters:
        rank (str, default="sudo"): rank needed to trigger a command
    """

    def decorators(coro):

        @wraps(coro)
        async def check(client, message):
            user_id = message.from_user.id
            if rank in ["owner", "sudo"] and user_id == Config.OWNER_ID:
                return await coro(client, message)
            elif rank == "sudo" and user_id in Config.SUDO_USERS:
                return await coro(client, message)
            else:
                LOGGER.error("Unkown rank \"%s\"", rank)
                return
                

        return check

    return decorators
