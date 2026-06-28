# Copyright (c) 2026 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual property of SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.

from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from YUKIREACTION import OWNER, YUKIREACTION


def is_admins(func: Callable) -> Callable:
    async def non_admin(c: YUKIREACTION, m: Message):
        if m.from_user.id == OWNER:
            return await func(c, m)

        admin = await c.get_chat_member(m.chat.id, m.from_user.id)
        if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await func(c, m)

    return non_admin



from .read import *
from .inline import *
