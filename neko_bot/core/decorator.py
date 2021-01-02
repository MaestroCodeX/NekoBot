"""This module for"""
from functools import wraps
from neko_bot import Config


async def adminlist(client, chat_id):
    """This Function to get admin list"""
    members = client.iter_chat_members(chat_id, filter="administrators")
    _admin = []
    async for i in members:
        _admin.append(i.user.id)
    return _admin


def admin(func):
    """This function build decorator for administ"""
    wraps(func)

    async def decorator(client, message):
        chat_id = message.chat.id
        administ = await adminlist(client, chat_id)
        if message.from_user.id in administ:
            await func(client, message)
        else:
            await message.reply_text("You are not an admin!")

    return decorator


def sudo(func):
    """This Function for filters user and staff bot"""
    wraps(func)

    async def decorator(client, message):
        user_id = message.from_user.id
        if user_id not in Config.OWNER_ID and Config.SUDO_USERS:
            return
        else:
            await func(client, message)

    return decorator
