import configparser
from disnake.ext import commands
import disnake
import random

#Define Cinfig
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

#Define Discord Variables
def Discord():
  config = read_config()
  ServerID = int(config['DiscordServer']['ServerID'])
  channel = int(config['Advert']['General'])
  return ServerID, channel

#Define if advertising enabled
def Advertising():
  config = read_config()
  enabled = bool(config['Advert']['Advertising'])
  return enabled

#Define Server Variables
def Server():
  config = read_config()
  ip = config['ServerSettings']['ip']
  port = int(config['ServerSettings']['port'])
  retry = int(config['ServerSettings']['retry'])
  timeout = int(config['ServerSettings']['timeout'])
  return ip, port, retry, timeout

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
  donate = config['Donate']['DonateURL']
  return donate

#Define Alert Methods
def Alerts():
  config = read_config()
  alert_check = config['StatusAlerts']['offline_alert']
  alert_channel = int(config['StatusAlerts']['admin_alert'])
  alert_admin = int(config['StatusAlerts']['ele_id'])
  return alert_check, alert_channel, alert_admin  

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

#Assign adverts
def advert():
  recovery = '<@1007106214875893770>'
  support = '<@1007106214875893770>'
  advert = ['You help us pay for the server, website, advertising, ddos protection & more. Type $donate to support the server.', 'To check who is online, use the /online command.', f'For game support, head to the {support} channel and click the ticket reaction to open a support ticket.', f'Need help recovering your account? Head to the {recovery.mention} channel and click on the ticket reation. One of our helpful admins will then help you recover your old account.']
  message = random.choice(advert)
  return message

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