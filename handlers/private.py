import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Hello, Welcome {message.from_user.mention()}

I am powerful easy to use TeleGram Super Bot. I can play high quality and unbreakable music in your group voice chat. Just add me and promote with needed powers.

Use Inline buttons for more !!
For Help : @StrayCoderSupport
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Add me to a Group ➕", url=f"https://t.me/{me_bot.username}?startgroup=true")
                ],[
                    InlineKeyboardButton("❓ Basic Guide", callback_data="user_guide")
                ],[
                    InlineKeyboardButton("📚 Commands", callback_data="command_list"),
                    InlineKeyboardButton("❤️ Donate", url=f"https://t.me/{OWNER_USERNAME}")
                ],[
                    InlineKeyboardButton("👥 Support Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton("📣 Support Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton("🌐 Source Code", url="https://github.com/levina-lab/video-stream")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bb7e6f59b3db29b215446.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://github.com/EsportMusicX/SmokerMusicX")
                ]
            ]
        ),
    )
