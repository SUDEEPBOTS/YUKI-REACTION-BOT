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

"""@YUKIREACTION.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        await message.react("👍")
    except Exception as e:
        print(f"Failed to react to message: {e}")"""

from telethon import TelegramClient, events


@YUKIREACTION.on(events.NewMessage(incoming=True))
async def react_to_messages(event):
    try:
        await event.message.respond("👍")  # Telethon में `send_reaction` अभी Stable Version में नहीं है
    except Exception as e:
        print(f"Failed to react to message: {e}")

