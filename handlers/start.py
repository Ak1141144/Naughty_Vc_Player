from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>โจ **๐๐ก๐๐ฅ๐๐จ๐ฆ๐ {message.from_user.first_name}** \n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ๐ฎ๐น๐น๐ผ๐ ๐๐ผ๐ ๐๐ผ ๐ฝ๐น๐ฎ๐ ๐บ๐๐๐ถ๐ฐ ๐ผ๐ป ๐ด๐ฟ๐ผ๐๐ฝ๐ ๐๐ต๐ฟ๐ผ๐๐ด๐ต ๐๐ต๐ฒ ๐ป๐ฒ๐ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ'๐ ๐๐ผ๐ถ๐ฐ๐ฒ ๐ฐ๐ต๐ฎ๐๐ ๐ฉ๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ ๐๐๐๐ง๐๐ฆ!**

๐ก **๐๐ถ๐ป๐ฑ ๐ผ๐๐ ๐ฎ๐น๐น ๐๐ต๐ฒ ๐๐ผ๐'๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฎ๐ป๐ฑ ๐ต๐ผ๐ ๐๐ต๐ฒ๐ ๐๐ผ๐ฟ๐ธ ๐ฏ๐ ๐ฐ๐น๐ถ๐ฐ๐ธ๐ถ๐ป๐ด ๐ผ๐ป ๐๐ต๐ฒ ยป ๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !**

โ **๐๐ผ๐ฟ ๐ถ๐ป๐ณ๐ผ๐ฟ๐บ๐ฎ๐๐ถ๐ผ๐ป ๐ฎ๐ฏ๐ผ๐๐ ๐ฎ๐น๐น ๐ณ๐ฒ๐ฎ๐๐๐ฟ๐ฒ ๐ผ๐ณ ๐๐ต๐ถ๐ ๐ฏ๐ผ๐, ๐ท๐๐๐ ๐๐๐ฝ๐ฒ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "๐ ๐ง ๐๐๐๐ก ๐๐ค๐ฃ๐ ๐ถ โจ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "๐ข สแดแดก แดแด แด๊ฑแด แดแด", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "๐ แดแดแดแดแดษดแด๊ฑ", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "๐ฅ ๐ฝ๐๐๐ฃ๐๐ข ๐", url=f"https://t.me/Badnam_xD")
                ],[
                    InlineKeyboardButton(
                        "๐ ๐๐ง๐ค๐ช๐ฅ ๐๐ฌ๐ฃ๐๐ง ๐", url=f"https://t.me/Nau_ghty_devil"
                    ),
                    InlineKeyboardButton(
                        "๐ก๐พ๐๐๐ฉ๐ฉ๐๐ฃ๐ ๐๐๐ง๐ซ๐๐ง๐", url=f"https://t.me/naughty_stud_ents")
                ],[
                    InlineKeyboardButton(
                        "๐ ๐ฝ๐๐๐ ๐", url="https://t.me/Atit_raj_188")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ ๐พ๐ค๐๐'๐จ ๐ซ", url="https://github.com/BadnamOp/Badnam_Vc_Player"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""โ **สแดแดษดแดแด ษช๊ฑ สแดษดษดษชษดษข**\n<b>๐? **แดแดแดษชแดแด:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โจ ๐พ๐๐๐ฉ๐ฉ๐๐ฃ๐ ๐๐ง๐ค๐ช๐ฅ", url=f"https://t.me/naughty_stud_ents"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ ๐๐๐๐ฃ๐ฃ๐๐ก", url=f"https://t.me/its_akku_about"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐๐ป **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands powered By Badnam!**

โก __Powered by {BOT_NAME} สแดแดษดแดแด""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="โ สแดแดก แดแด แด๊ฑแด แดแด", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐ก Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

โก __Powered by {BOT_NAME} Badnam__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โก ๐ฝ๐๐จ๐๐ ๐๐จ๐", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "โฃ๏ธ ๐ผ๐๐ซ๐๐ฃ๐๐ ๐๐จ๐", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐ผ๐๐ข๐๐ฃ ๐๐จ๐", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "โฒ๏ธ ๐๐ช๐๐ค ๐๐จ๐", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐ฌ๐ฃ๐๐ง ๐๐จ๐", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐ช๐ฃ ๐๐จ๐", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("แดข แดษชษดษดษข...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "๐ฃ `แดแดษดษข!!`\n"
        f"๐ง   `{delta_ping * 1000:.3f} แด๊ฑ`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ค สแดแดษดแดแด ๊ฑแดแดแดแด๊ฑ:\n"
        f"โข **แดแดแดษชแดแด:** `{uptime}`\n"
        f"โข **๊ฑแดแดสแด แดษชแดแด:** `{START_TIME_ISO}`"
    )
