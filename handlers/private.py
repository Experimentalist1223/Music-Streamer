import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**Hello, Welcome {message.from_user.mention()}

I am powerful easy to use TeleGram Super Bot. I can play high quality and unbreakable music in your group voice chat. Just add me and promote with needed powers.

Use Inline buttons for more !!
For Help : @StrayCoderSupport**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✚ Add me to your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("👤 Bot Owner", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("📢 Source Code", url=f"https://t.me/StrayCoder")
                ],[
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/StrayCoderSupport"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/StrayCoder")
                ],[
                    InlineKeyboardButton("🔍 How To Use? Commands", callback_data="cb_cmd")
                ],
            ]
        ),
    )
    

@Client.on_message(command(["repo"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""`Click on the given button to get the Source Code of the Bot !!`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Source Code", url=f"https://github.com/EsportMusicX/SmokerMusicX")
                ]
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**× I am Alive ×**\n\n@StrayCoder 📡")


@Client.on_message(command(["start"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""**Thanks for adding me im your Group ❤️ Now promote me as a admin with needed powers otherwise I am not able to work properly !!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Source Code", url=f"https://github.com/EsportMusicX/SmokerMusicX")
                ],[
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/StrayCoderSupport"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/StrayCoder")
                  ],
            ]
        ),
    )
