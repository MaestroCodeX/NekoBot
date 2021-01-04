"""Chat action decorators"""

from functools import wraps
from typing import Optional


def chat_action(action: Optional[str] = "typing"):
    """Trigger an action on function call.

    Parameters:
        rank (str, default="typing"): action type to send
            list of available action at https://docs.pyrogram.org/api/methods/send_chat_action
    """

    def decorators(coro):

        @wraps(coro)
        async def send_action(client, message, *args, **kwargs):
            await client.send_chat_action(message.chat.id, action)
            return await coro(client, message,  *args, **kwargs)

        return send_action

    return decorators