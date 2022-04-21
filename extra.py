@Client.on_message(command(["start"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**Thanks for adding me im your Group ❤️ Now promote me as a admin with needed powers otherwise I am not able to work properly !!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Source Code", url=f"https://github.com/TheStrayCoder/Music-Streamer")
                ],[
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/StrayCoderSupport"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/StrayCoder")
                  ],
            ]
        ),
    )
