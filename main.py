import os
from config import Config
from pyrogram import Client as GREYMATTER , idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Auth Users
AUTH_USERS = [ int(chat) for chat in Config.AUTH_USERS.split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")
if __name__ == "__main__" :
    GreyMatterBot = GREYMATTER(
        "GreyMatterBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=plugins
    )
    
    async def main():
        await GreyMatterBot.start()
        bot_info  = await GreyMatterBot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) GREYMATTER --->")
        await idle()
    
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info(f"<---Bot Stopped-->")
