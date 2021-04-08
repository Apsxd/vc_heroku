from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""[★](https://telegra.ph/file/740f87cbf8ef39d7af03d.png)I am **{bn}** A telegram voice chat bot for playing songs in your group voice chat
Click [commands](https://telegra.ph/MUSIC-BOT-COMMAND-04-08) to look at bot commands
add assistant user bot after adding bot to groups you can get it by clicking [GROUP] button
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE CODE", url="https://github.com/zyrus-basi/vc_heroku"
                    ),
                    InlineKeyboardButton(
                        "GROUP||ASSISTANT", url="https://t.me/unitedbotsupport"
                    )
                ]
            ]
        )
    )
