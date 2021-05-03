from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
f""",I am **{bn}** A telegram voice chat bot for playing songs in your group voice chat.
Click [COMMANDS](https://telegra.ph/MUSIC-BOT-COMMAND-04-08) For a takeup on commands.
Join our support group for getting manual about how adding to your group
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE CODE", url="https://github.com/basi-mon/vc_heroku"
                    ),
                    InlineKeyboardButton(
                        "GROUP", url="https://t.me/unitedbotsupport"
                    ),
                    Inlinekeyboardbutton(
                         "ASSISTANT", url=" https://t.me/bliss_robot"
                    )
                ]
            ]
        )
    )
