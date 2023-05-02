import os
from os import getenv

from telethon import TelegramClient as tc
import logging
from dotenv import load_dotenv as lv
from rich.console import Console


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

if os.path.exists("local.env"):
  lv('local.env')
  
lv()
c = Console()
# module.
MOD_LOAD = []
MOD_NOLOAD = []

API_ID = int(getenv("API_ID", 1))
API_HASH = getenv('API_HASH')
BOT_TOKEN = getenv('BOT_TOKEN')
AUTH_USER = list(int(getenv("AUTH_USER")))


bot = tc('Shashank', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


async def whoami():
  me = await bot.get_me()
  c.print(
    "[red] Bot client has been started\n\nUser id - {}\nUsername - {}".format(
      me.id,
      me.username
    )
  )