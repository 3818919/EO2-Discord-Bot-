import os
import config
from api import server
import asyncio
import disnake
from disnake.ext import tasks, commands


class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class advert:
  enabled = config.Advertising()
  ServerID, channel = config.Discord()
  
TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned)
bot.remove_command('help')

Server = ".:Fallen Evolution:."
print (bcolours.GREEN + Server)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
  else:
    pass

#Checks players & server online & updates status
@tasks.loop(seconds=30)
async def status_swap(): 
  plist, pnum, game = server.eo2()
  await bot.change_presence(status=disnake.Status.online, activity=game)

@tasks.loop(minutes=180)
async def send():
  await asyncio.sleep(200)
  channel = bot.get_channel(advert.channel)
  try:
    if advert.enabled == True:
      message = config.advert()
      await channel.send(message, delete_after = 1800)
      return
    else:
      print (bcolours.RED + 'Advertising is disabled')
  except:
    return


@send.before_loop
async def before():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
  if not status_swap.is_running():
    print('Status Updater Loaded')
    status_swap.start()
  if not send.is_running():
    print('Adverts Loaded')
    send.start()
  print(bcolours.YELLOW + 'I have logged in to the EO2 Discord as {0.user}'.format(bot))
  

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
      
    await bot.process_commands(message)

#Uncomment the below line to enable config.ini token functionality
#TOKEN = config.TOKEN()
bot.run(TOKEN)