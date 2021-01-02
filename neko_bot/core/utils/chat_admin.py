async def adminlist(client, chat_id):
    """This Function to get admin list."""
    members = client.iter_chat_members(chat_id, filter="administrators")
    _admin = []
    async for i in members:
        _admin.append(i.user.id)
    return _admin