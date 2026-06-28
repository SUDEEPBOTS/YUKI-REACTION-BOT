# Copyright (c) 2026 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual property of SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.

from pyrogram import Client, filters
from pyrogram.types import Message
from YUKIREACTION import YUKIREACTION

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}! 👋\n\n"
        "I'm your Reaction Bot! I'll react to every message in groups, channels, and private chats with a 👍 emoji.\n\n"
        "Add me to your group or channel and watch me in action! 🚀\n\n"
        "**You can make your bot by /clone😁**"
    )
