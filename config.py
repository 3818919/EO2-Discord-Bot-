import configparser
from disnake.ext import commands
import disnake
import random

#Define COnfig
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

################################
#### DEBUG Related Settings ####
################################

#Define Discord Variables
def DEBUG():
  config = read_config()
  testchannel = int(config['DEBUG']['testchannel'])
  return testchannel

##################################
#### Discord Related Settings ####
##################################

#Define Discord Variables
def Discord():
  config = read_config()
  ServerID = int(config['DiscordServer']['ServerID'])
  channel = int(config['Advert']['General'])
  return ServerID, channel

#Define TOKEN from config.ini if Enabled
def TOKEN():
  config = read_config()
  enabled = bool(config['token']['enabled'])
  if enabled == True:
    TOKEN = bool(config['token']['token'])
    return TOKEN
  else:
    print('TOKEN is not enabled')

#Defind Bot Attributes
def bot():
  bot = commands.Bot(
  command_prefix='/',
  test_guilds=[1007103496262258699,828442977134182401])
  return bot

#Define Bot Intents
def dbot():
  intents = disnake.Intents.default()
  intents.message_content = True
  intents.typing = False
  intents.presences = False
  bot = commands.Bot(command_prefix='/', intents=intents, case_insensitive=True,)
  return bot

###################
## Auto Messages ##
###################

#Welcome Message for new members
def Welcome(member):
  member = member.mention
  messages = [f'{member} has entered the chat! Hope you brought 🍕', f'{member} has joined the party! 🥳', f'{member} has arrived right in the nick of time!', f'Have no fear {member} is here!']
  welcome = random.choice(messages)
  return welcome

#Define if advertising enabled
def Advertising():
  config = read_config()
  active = config['Advert']['active']
  if active == "True" or active == "true":
    active = True
    return active
  else:
    active = False
    return active

###########################
#### EO2 Game Settings ####
###########################

#Define Server Variables
def Server():
  config = read_config()
  ip = config['ServerSettings']['ip']
  port = int(config['ServerSettings']['port'])
  retry = int(config['ServerSettings']['retry'])
  timeout = int(config['ServerSettings']['timeout'])
  return ip, port, retry, timeout

################################
## Server Down Discord Alerts ##
################################

#Define Alert Methods
def Alerts():
  config = read_config()
  alert_check = config['StatusAlerts']['offline_alert']
  alert_channel = int(config['StatusAlerts']['admin_alert'])
  alert_admin = int(config['StatusAlerts']['ele_id'])
  return alert_check, alert_channel, alert_admin 

#Define server online info
def online(pnum):
  title = 'Server Online'
  desc = 'I have just checked and EO2 is online!'
  info = f'There are {pnum} people online'
  return title, desc, info

#Define server offline info
def offline():
  title = 'Server Offline'
  desc = 'I have just checked and EO2 is currently offline!'
  return title, desc

############################
## Web Scraping Functions ##
############################

#Define Website Connection Variables
def API():
  config = read_config()
  domain = config['Website']['domain']
  ranks = config['Website']['toplist']
  return domain, ranks

#Define Download Link
def download():
  config = read_config()
  download = config['ClientDownload']['DownloadURL']
  return download

#Define Donate Link
def donate():
  config = read_config()
  donate = str(config['Donate']['DonateURL'])
  thanks = str(config['Donate']['Thanks'])
  return donate, thanks
