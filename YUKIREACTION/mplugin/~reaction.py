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
import random

EMOJIS = ["🥰", "❤️", "😁", "💋", "😱", "🤣", "😘", "❤️‍🔥", "👌", "🫡", "😍"]

@Client.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        random_emoji = random.choice(EMOJIS)
        await message.react(random_emoji)
    except Exception as e:
        print(f"Failed to react to message: {e}")
