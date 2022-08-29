import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس صاصا","سورس","السورس","يا سورس"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/555865464bdc020e04fce.jpg",
        caption=f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 sasa .](https://t.me/indexaty)\n\n[❍ | sasa 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/indexaty)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/indexaty)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "َِ𝙈 َِ𝙊 َِ𝙎 َِ𝙏 َِ𝘼 َِ𝙁 َِ𝘼 🖤", url=f"https://t.me/p_q_z"),
                    InlineKeyboardButton(
                        "◜ 𝙈𝙞 𝙄𝙭 𝙓 ◞", url=f"https://t.me/l_Mix_1"),
                ],[
                    InlineKeyboardButton(
                        "- 𝐒𝐨𝐮𝐫𝐜𝐞 sasa .", url=f"https://t.me/indexaty"),
                    InlineKeyboardButton(
                        "- 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 sasa .", url=f"https://t.me/p_q_z"),
                ],[
                    InlineKeyboardButton(
                        "- ضيف البوت لمجموعتك .", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],

            ]

        ),

    )
