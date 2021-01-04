from pyrogram import Client


class RawClient(Client):
    """ NekoBot raw client """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)