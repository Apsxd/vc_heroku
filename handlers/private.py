from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!

COMMANDS
 /play - Plays the replied audio file or YouTube video through link.
 /pause - Pause Voice Chat Music.
 /resume - Resume Voice Chat Music.
 /skip - Skips the current Music Playing In Voice Chat.
 /stop - Clears The Queue as well as ends Voice Chat Music.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE CODE", url="https://github.com/zyrus-basi/vc_heroku"
                    ),
                    InlineKeyboardButton(
                        "GROUP", url="https://t.me/uniedbotsupport"
                    )
                ]
            ]
        )
    )
