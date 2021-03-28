from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!

iam a telegram music bot i play music on voice chat on telegram groups [☺️](https://telegra.ph/file/5151877cfe274d2c78ac7.jpg)
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ADD ME TO GROUPS", url="https://t.me/heyyoheyyo"
                    ),
                    InlineKeyboardButton(
                        "OWNER", url="https://t.me/AwAlKeR96"
                    )
                ]
            ]
        )
    )
