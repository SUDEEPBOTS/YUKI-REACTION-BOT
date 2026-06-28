# © 2026 HellfireDevs / SUDEEPBOTS
# All Rights Reserved.

from pyrogram import Client, filters
from pyrogram.types import Message
from YUKIREACTION import YUKIREACTION

@YUKIREACTION.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}! 👋\n\n"
        "I'm your Reaction Bot! I'll react to every message in groups, channels, and private chats with a 👍 emoji.\n\n"
        "Add me to your group or channel and watch me in action! 🚀\n\n"
        "**You can make your bot by /clone😁**"
    )
    
