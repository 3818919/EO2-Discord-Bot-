import configparser
from disnake.ext import commands
import disnake
import pandas as pd
from urllib.request import Request, urlopen

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def Discord():
  config = read_config()
  ServerID = int(config['DiscordServer']['ServerID'])
  advertising = bool(config['Advert']['Advertising'])
  channel = int(config['Advert']['General'])
  return ServerID, advertising, channel


def Server():
  config = read_config()
  ip = config['ServerSettings']['ip']
  port = int(config['ServerSettings']['port'])
  retry = int(config['ServerSettings']['retry'])
  timeout = int(config['ServerSettings']['timeout'])
  return ip, port, retry, timeout

def API():
  config = read_config()
  domain = config['Website']['domain']
  ranks = config['Website']['toplist']
  discord = config['Website']['discord']
  download = config['Website']['client']
  online = str(config['Website']['SLN'])
  backup = config['Website']['backup']
  return domain, ranks, discord, download, online, backup

def Alerts():
  config = read_config()
  alert_check = config['StatusAlerts']['offline_alert']
  alert_channel = int(config['StatusAlerts']['admin_alert'])
  alert_admin = int(config['StatusAlerts']['ele_id'])
  return alert_check, alert_channel, alert_admin  

def bot():
  bot = commands.Bot(
  command_prefix='/',
  test_guilds=[1007103496262258699,828442977134182401])
  return bot

def dbot():
  intents = disnake.Intents.default()
  intents.message_content = True
  intents.typing = False
  intents.presences = False
  bot = commands.Bot(command_prefix='/', intents=intents, case_insensitive=True,)
  return bot

def topPlayers():
  domain, ranks, discord, download, online, backup = API()
  req = Request(ranks, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  data = pd.read_html(webpage)[0]
  data.index += 1
  data = data.head(100) #Only show 20 Items
  People = data.Name
  Levels = data.Level
  Names = People.values
  Levels = Levels.values
  return Names, Levels