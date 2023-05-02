import glob
import os
from pathlib import Path
from core.utilities import load_plugins
from rich.console import Console

from rich.table import Table 

from . import bot, whoami

c = Console()
path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
  with open(name) as n:
    patt = Path(n.name)
    plugin_name = patt.stem
    load_plugins(plugin_name.replace(".py", ""))

      
c.print('[red]SUCCESSFULLY DEPLOYED BOT')

if __name__ == '__main__':
  bot.loop.run_until_complete(whoami())
  bot.run_until_disconnected()