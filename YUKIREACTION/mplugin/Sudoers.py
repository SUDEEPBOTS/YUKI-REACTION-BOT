# © 2026 HellfireDevs / SUDEEPBOTS
# All Rights Reserved.

from pyrogram import filters, Client
from pyrogram.types import Message

from config import MONGO_URL, OWNER_ID
from YUKIREACTION import YUKIREACTION as app
from YUKIREACTION import SUDOERS
from YUKIREACTION.database import add_sudo, remove_sudo

@Client.on_message(filters.command("addsudo") & filters.user(OWNER_ID))
async def useradd(client, message: Message):
    if MONGO_URL is None:
        return await message.reply_text(
            "**Dᴜᴇ ᴛᴏ ʙᴏᴛ's ᴘʀɪᴠᴀᴄʏ ɪssᴜᴇs, Yᴏᴜ ᴄᴀɴ'ᴛ ᴍᴀɴᴀɢᴇ sᴜᴅᴏ ᴜsᴇʀs ᴡʜᴇɴ ʏᴏᴜ'ʀᴇ ᴜsɪɴɢ Yᴜᴋᴋɪ's Dᴀᴛᴀʙᴀsᴇ.\n\nPʟᴇᴀsᴇ ғɪʟʟ ʏᴏᴜʀ MONGO_DB_URI ɪɴ ʏᴏᴜʀ ᴠᴀʀs ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await client.get_users(user)
        if user.id in SUDOERS:
            return await message.reply_text(f"{user.mention} ɪs ᴀʟʀᴇᴀᴅʏ ᴀ sᴜᴅᴏ ᴜsᴇʀ.")
        added = await add_sudo(user.id)
        if added:
            SUDOERS.add(user.id)
            await message.reply_text(f"ᴀᴅᴅᴇᴅ **{user.mention}** ᴛᴏ sᴜᴅᴏ ᴜsᴇʀs.")
        else:
            await message.reply_text("ғᴀɪʟᴇᴅ")
        return
    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            f"{message.reply_to_message.from_user.mention} ɪs ᴀʟʀᴇᴀᴅʏ ᴀ sᴜᴅᴏ ᴜsᴇʀ."
        )
    added = await add_sudo(message.reply_to_message.from_user.id)
    if added:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            f"ᴀᴅᴅᴇᴅ **{message.reply_to_message.from_user.mention}** ᴛᴏ sᴜᴅᴏ ᴜsᴇʀs."
        )
    else:
        await message.reply_text("ғᴀɪʟᴇᴅ")
    return


@Client.on_message(filters.command(["rmsudo", "delsudo"]) & filters.user(OWNER_ID))
async def userdel(client, message: Message):
    if MONGO_URL is None:
        return await message.reply_text(
            "**Dᴜᴇ ᴛᴏ ʙᴏᴛ's ᴘʀɪᴠᴀᴄʏ ɪssᴜᴇs, Yᴏᴜ ᴄᴀɴ'ᴛ ᴍᴀɴᴀɢᴇ sᴜᴅᴏ ᴜsᴇʀs ᴡʜᴇɴ ʏᴏᴜ'ʀᴇ ᴜsɪɴɢ Yᴜᴋᴋɪ's Dᴀᴛᴀʙᴀsᴇ.\n\nPʟᴇᴀsᴇ ғɪʟʟ ʏᴏᴜʀ MONGO_DB_URI ɪɴ ʏᴏᴜʀ ᴠᴀʀs ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await client.get_users(user)
        if user.id not in SUDOERS:
            return await message.reply_text("ɴᴏᴛ ᴀ ᴘᴀʀᴛ ᴏꜰ ʙᴏᴛ's sᴜᴅᴏ.")
        removed = await remove_sudo(user.id)
        if removed:
            SUDOERS.remove(user.id)
            await message.reply_text("ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ʙᴏᴛ's sᴜᴅᴏ ᴜsᴇʀ.")
            return
        await message.reply_text("sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ")
        return
    user_id = message.reply_to_message.from_user.id
    if user_id not in SUDOERS:
        return await message.reply_text("ɴᴏᴛ ᴀ ᴘᴀʀᴛ ᴏꜰ ʙᴏᴛ's sᴜᴅᴏ.")
    removed = await remove_sudo(user_id)
    if removed:
        SUDOERS.remove(user_id)
        await message.reply_text("ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ʙᴏᴛ's sᴜᴅᴏ ᴜsᴇʀ.")
        return
    await message.reply_text("sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ.")


@Client.on_message(filters.command(["sudo", "sudolist"]))
async def sudoers_list(client, message: Message):
    text = "🔥<u> **ᴏᴡɴᴇʀ:**</u>\n"
    count = 0
    try:
        user = await client.get_users(OWNER_ID)
        user_name = user.first_name if not user.mention else user.mention
        count += 1
        text += f"{count}➤ {user_name}\n"
    except Exception:
        pass

    smex = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await client.get_users(user_id)
                user_name = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n🔥<u> **sᴜᴅᴏᴇʀs:**</u>\n"
                count += 1
                text += f"{count}➤ {user_name} ({user.id})\n"
            except Exception:
                continue

    if not text:
        await message.reply_text("ɴᴏ sᴜᴅᴏ ᴜsᴇʀs ғᴏᴜɴᴅ.")
    else:
        await message.reply_text(text)
