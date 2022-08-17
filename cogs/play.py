import disnake
from disnake.ext import commands
import config
from api import api, server
import time

class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class info:
  plist, pnum, game = server.eo2()
  client = api.download()

class play(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  bot = config.dbot()  
  @bot.slash_command(description="A quick way to download the game.")
  async def play(inter):
    download = disnake.Embed(title = 'Play EO2!', url=info.client, description = f'Currently {info.pnum} players online!', colour = disnake.Colour.green())
    download.set_thumbnail(url="https://endlessonline2.com/npcs/4781.png")
    await inter.response.send_message(embed=download)
    time.sleep(2)


def setup(bot):
  bot.add_cog(play(bot))
  print (bcolours.GREEN + 'Play Command Loaded')