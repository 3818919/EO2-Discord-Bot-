import disnake
from disnake.ext import commands
import config
from api import api
import time

class rank:
  ServerID, channel = config.Discord()

class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class TopList(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  bot = config.dbot()  
  @bot.slash_command(description="Check the players with the highest levels.")
  async def toplist(inter):
    Names, Levels = api.topPlayers()
    Names = '\n'.join(map(str, Names))
    Levels = '\n'.join(map(str, Levels))
    toplist = disnake.Embed(title = 'Top 100 Players',description = 'Type / to see my commands.', colour = disnake.Colour.green())
    toplist.add_field(name='Name', value=Names, inline=True)
    toplist.add_field(name='Level', value=Levels, inline=True)
    await inter.response.send_message(embed=toplist, delete_after=120)
    time.sleep(2)

def setup(bot):
  bot.add_cog(TopList(bot))
  print (bcolours.GREEN + 'Toplist Command Loaded')