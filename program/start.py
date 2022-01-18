from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAEECP1hoQ3WiZmIgZ1M6zpI4tagFYi5AQACcQsAArp60VE-Obmr9D4hkiIE")
    await message.reply_text(
        f"""✨ **ᴡᴇʟᴄᴏᴍᴇ {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴏɴ ɢʀᴏᴜᴘs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ɴᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ's ᴠɪᴅᴇᴏ ᴄʜᴀᴛs!**

💡 **ғɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚 ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!**

🔖 **🔖 ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ, ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ » ❓ ʙᴀsɪᴄ ɢᴜɪᴅᴇ ʙᴜᴛᴛᴏɴ!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "乂ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ乂",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("乂ʙᴀsɪᴄ ɢᴜɪᴅᴇ乂", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("乂ᴄᴏᴍᴍᴀɴᴅs乂", callback_data="cbcmds"),
                    InlineKeyboardButton("乂ᴄʀᴇᴀᴛᴏʀ乂", url=f"https://t.me/Xmartperson"),
                ],
                [
                    InlineKeyboardButton(
                        "乂ʙᴏᴛ ɢʀᴏᴜᴘ乂", url=f"https://t.me/Rockerz_support"
                    ),
                    InlineKeyboardButton(
                        "乂ʙᴏᴛ ᴄʜᴀɴɴᴇʟ乂", url=f"https://t.me/Rockerz_updates"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "乂sɪɴɢɪɴɢ sᴜᴘᴘᴏʀᴛ乂", url=f"https://t.me/Singing_music_Idol"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("乂ʙᴏᴛ ɢʀᴏᴜᴘ乂", url=f"https://t.me/Rockerz_updates"),
                InlineKeyboardButton(
                    "乂ʙᴏᴛ ᴄʜᴀɴɴᴇʟ乂", url=f"https://t.me/Rockerz_Updates"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [▁▂▄▅▆▇█ 𝕃𝕖𝕘𝕖𝕟𝕕◇𝕊𝕒𝕝𝕚𝕞 █▇▆▅▄▂▁](https://t.me/Xmartperson)\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group video chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `ᴘᴏɴɢ!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
