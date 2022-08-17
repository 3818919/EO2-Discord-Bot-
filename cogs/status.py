import disnake
from disnake.ext import commands
import config
from api import api, server
import time

class eo2D:
  ServerID, channel = config.Discord()
  plist, pnum = api.players()
  title, desc, info = config.online(pnum)

class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class status(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  bot = config.dbot()  
  @bot.slash_command(description="Checks the stats of an item in game - /item <name>")
  async def online(inter):
    status = server.ping()
    if status == True:
     
      check = disnake.Embed(title = eo2D.title, description = eo2D.desc, colour = disnake.Colour.green())
      check.add_field(name=f"{eo2D.pnum} Players Online", value=eo2D.plist, inline=False)
      await inter.response.send_message(embed=check)
      time.sleep(2)
    else:
      title, desc = config.offline()
      check = disnake.Embed(title = eo2D.title, description = eo2D.desc, colour = disnake.Colour.green())
      check.add_field(name=f"{eo2D.pnum} Players Online", value=eo2D.plist, inline=False)
      await inter.response.send_message(embed=check)
      time.sleep(2)

def setup(bot):
  bot.add_cog(status(bot))
  print (bcolours.GREEN + 'Online Command Loaded')