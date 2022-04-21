from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
        await query.edit_message_text(
              f"""ʜᴇʟʟᴏ [✨]({START_PIC}) **ᴡᴇʟᴄᴏᴍᴇ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
 **ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄᴀʟʟ !!**
 **ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ 💫**
 **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴊᴏɪɴ @Techno_Trickop**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛓ Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ Gʀᴏᴜᴘ ⛓",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("• Cᴏᴍᴍᴀɴᴅs •",  callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton(
                    "• Oᴡɴᴇʀ •", 
                    url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("• Dᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/herox_xd"),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "• Uᴘᴅᴀᴛᴇs •", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴏᴜʀᴄᴇ Cᴏᴅᴇ •", url="https://github.com/SJMxADITI/TrickyAbhi-Music"
                    )
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cb_cmd"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**here is some commands**
𝙎𝙞𝙢𝙥𝙡𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 
•  `/play (song name)` 
•  `/skip` - skip the current song
•  `/end` - stop music play
•  `/pause` - pause song play
•  `/resume` - resume song play
•  `/mute` - mute assistant in vc
•  `/lyrics (song name)`
𝙁𝙪𝙣 𝙘𝙤𝙢𝙢𝙖𝙣𝙙
• `/truth` 🌝
• `/dare`  🌝
• `/sjm`    🌝
• `/abhi`   🌝
• `/tricky` 🌝
𝙀𝙭𝙩𝙧𝙖 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨
• `/ping` pong !!
• `/start` - Alive msg ~group 
• `/id` - Find out your grp and your id // stickers id also
• `/uptime` - 💻
• `/rmd` clean all downloads
• `/clean` - clear storage 
⚡ Powered By [H E R O X](https://t.me/herox_xd) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ Back", callback_data="cb_start")]]
        ),
    )
