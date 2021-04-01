from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""[★](https://telegra.ph/file/740f87cbf8ef39d7af03d.png)I am **{bn}** A telegram voice chat bot for playing songs in your group voice chat
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                        [
                            InlineKeyboardButton(
                                text="ADD ME TO GROUP",
                                url="t.me/{}?startgroup=true".format(
                                    context.bot.username
                                ),
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="SUPPORT",
                                url=f"https://t.me/unitedbotsupport",
                            ),
                            InlineKeyboardButton(
                                text="SOURCE CODE",
                                url="https://github.com/Basi-mon/vc_heroku",
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="COMMANDS||GUIDE",
                                url="https://t.me/nimmisupport/47",
                            )
                        ],
                    ]
                ),
            )
