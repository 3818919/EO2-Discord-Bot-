import config
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen

class config:
  domain, ranks = config.API()
  ip, port, retry, timeout = config.Server()
  download = config.download()

def topPlayers():
  req = Request(config.ranks, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  data = pd.read_html(webpage)[0]
  data.index += 1
  data = data.head(100) #Only show 20 Items
  People = data.Name
  Levels = data.Level
  Names = People.values
  Levels = Levels.values
  return Names, Levels

#Scrape website for download link
def download():
  download = config.download
  req = Request(download, headers={'User-Agent': 'Mozilla/5.0'})
  parser = 'lxml'  
  resp = urllib.request.urlopen(req)
  soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
  for link in soup.find_all('a', href=True):
    client = link['href']
    if client.endswith('msi'):
      return client

def players():
  try:
    Players = pd.read_html('http://101.98.189.250/eosource.net/characters.php?ip=game.endlessonline2.com&port=8079')[0]
    Players.index += 1
    Lists = Players.head(100) #Only show x Items
    People = Lists.Name
    People = sorted(People)
    Names = People.values
    plist = '\n '.join(Names) #List of Players
    pnum = len(Names) #Count of players
    return plist, pnum
  except:
    Table = pd.read_html('http://www.apollo-games.com/SLN/sln.php/onlinelist?server=host:game.endlessonline2.com:8079')[0]
    Table.index += 1
    List2 = Table.head(100) #Only show x Items
    People_Names = List2.Name
    Names = People_Names.values
    plist = '\n '.join(Names) #List of Players
    pnum = len(Names) #Count of players
    return plist, pnum