from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
f""",I am **{bn}** A telegram voice chat bot for playing songs in your group voice chat.
Click commands For a takeup on commands.
Join our support group for getting manual about how adding to your group
        """,
        reply_markup=InlineKeyboardMarkup(
             [
                [
                    InlineKeyboardButton(
                        "source || commands", url="https://telegra.ph/MUSIC-BOT-COMMAND-04-08"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/unitedbotsupport"
                    ),
                    InlineKeyboardButton(
                        "assistant", url="https://t.me/bliss_robot"
                    )
                ]
            ]
        )
    )
