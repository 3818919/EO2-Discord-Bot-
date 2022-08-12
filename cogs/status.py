import disnake
from disnake.ext import commands
from config import config, server
import time

class eo2D:
  ServerID, advertising, channel = config.Discord()
  plist, pnum, game = server.eo2()

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
      title, desc, info = server.online(eo2D.pnum)
      check = disnake.Embed(title = title,description = desc, colour = disnake.Colour.green())
      check.add_field(name=info, value=eo2D.plist, inline=False)
      await inter.response.send_message(embed=check)
      time.sleep(2)
    else:
      title, desc = server.offline()
      check = disnake.Embed(title = title,description = desc, colour = disnake.Colour.green())
      check.add_field(name=info, value=eo2D.plist, inline=False)
      await inter.response.send_message(embed=check)
      time.sleep(2)

def setup(bot):
  bot.add_cog(status(bot))
  print (bcolours.GREEN + 'Online Command Loaded')