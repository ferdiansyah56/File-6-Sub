"""Get id of the replied user
Syntax: /id"""

from pyrogram import filters
from pyrogram.types import Message

from bot import Bot


@Bot.on_message(filters.command("id") & filters.private)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(
            f"User ID anda adalah: `{user_id}`", quote=True
        )

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += f"👥 Chat ID: `{message.chat.id}`"
        if message.reply_to_message:
            _id += f"🙋‍♂️ Replied User ID: `{message.reply_to_message.from_user.id}`"
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "👤 User ID: `{message.from_user.id}`"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"{file_info.message_type}: "
                f"`{file_info.file_id}`\n"
            )
        await message.reply_text(_id, quote=True)


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj
