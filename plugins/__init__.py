from pyrogram import filters
from pyrogram import Client as GreyMatter
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import os
import sys


@GreyMatter.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("start", prefixes=prefixes)
)
async def Start_msg(bot: GreyMatter , m: Message):
    await bot.send_photo(
    m.chat.id,
    photo="https://telegra.ph/file/19eeb26fa2ce58765917a.jpg",
    caption = f"Hello [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n" +
    f"\nI am Forward bot." +
    f"\nPress /help for More Info.\n\n__**Owner** : @GreyMatter_Owner\n**Language** : Python\n**Framwork** : Pyrogram__",
    # parse_mode="md",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Owner", url="https://t.me/GreyMatter_Owner")],
            [InlineKeyboardButton("Channel", url="https://t.me/GreyMatter_Bots")],
            [InlineKeyboardButton("YT Channel", url="https://youtube.com/@greymattersyt")],
        ],
    )
    )


@GreyMatter.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("help", prefixes=prefixes)
)
async def help_msg(bot: GreyMatter , m: Message):   
    await bot.send_message(
        m.chat.id,
        f"**(c) @GreyMatter_Bots**" +
        f"\n\nI can Forward message from one chat to another\n"+
        f"Available Commands are :"+
        f"\n\n/greymatter to start forwarding\n/log - To get Log file\n/restart - To Restart the bot"
    )

@GreyMatter.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("restart", prefixes=prefixes)
)
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@GreyMatter.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("log", prefixes=prefixes)
)
async def log_msg(bot: GreyMatter , m: Message):   
    await bot.send_document(m.chat.id, "log.txt")
