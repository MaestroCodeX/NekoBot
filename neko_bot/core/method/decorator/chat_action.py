from functools import wraps
from typing import Optional

from pyrogram import Client

class SendAction(Client):
    def send_action(
        self = None,
        action: Optional[str] = "typing",
    ):
        """Trigger an action on function call.

        Example: @neko.send_action("playing")

        Parameters:
            action (``str`` default="typing"): action type to send
                list of available action at https://docs.pyrogram.org/api/methods/send_chat_action
        """

        def decorator(coro):

            @wraps(coro)
            async def send(self, message, *args, **kwargs):
                await self.send_chat_action(message.chat.id, action)
                return await coro(self, message,  *args, **kwargs)

            return send

        return decorator