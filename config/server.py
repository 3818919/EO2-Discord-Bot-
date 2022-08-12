import os
from config import config
import socket
import disnake
import pandas as pd
import random
import lxml
from bs4 import BeautifulSoup

def ping():
  ip, port, retry, timeout = config.Server()
  alert_check, alert_channel, alert = config.Alerts()

  def isOpen(ip, port):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(timeout)
      try:
          s.connect((ip, int(port)))
          s.shutdown(socket.SHUT_RDWR)
          return True
      except:
          return False
      finally:
          s.close()

  def checkHost(ip, port):
      ipup = False
      for i in range(retry):
          if isOpen(ip, port):
              ipup = True
              break
          else:

              return
      return ipup
  if checkHost(ip, port):
    status = True
    return status
  else:
    status = False
    return status

def eo2():
  status = ping()
  try:
    if status == True:
      online = config.API() #Connected to eosource in config.ini
      Players = pd.read_html('http://101.98.189.250/eosource.net/characters.php?ip=game.endlessonline2.com&port=8079')[0]
      Players.index += 1
      Lists = Players.head(100) #Only show x Items
      People = Lists.Name
      People = sorted(People)
      Names = People.values
      plist = '\n '.join(Names) #List of Players
      pnum = len(Names) #Count of players
  
      if pnum ==1:
        game = disnake.Game(f'EO2 - {pnum} Player Online [{plist}]')
        return plist, pnum, game
      else:
        game = disnake.Game(f'EO2 - {pnum} Players Online [{plist}]')
        return plist, pnum, game
    else:
      game = disnake.Game('Nothing - Server Offline')
      return plist, pnum, game
    
  except:
    if status == True:
      Table = pd.read_html('http://www.apollo-games.com/SLN/sln.php/onlinelist?server=host:game.endlessonline2.com:8079')[0]
      Table.index += 1
      List2 = Table.head(100) #Only show x Items
      People_Names = List2.Name
      Names = People_Names.values
      plist = '\n '.join(Names) #List of Players
      pnum = len(Names) #Count of players

      if pnum ==1:
        game = disnake.Game(f'EO2 - {pnum} Player Online [{plist}]')
        return plist, pnum, game
      else:
        game = disnake.Game(f'EO2 - {pnum} Players Online [{plist}]')
        return plist, pnum, game
    else:
      game = disnake.Game('Nothing - Server Offline')
      return plist, pnum, game
      
def advert():
  advert = ['You help us pay for the server, website, advertising, ddos protection & more. Type $donate to support the server.', 'To check who is online, type $online.', 'For game support, head to the #support channel and click the ticket reaction to open a support ticket.', 'Need help recovering your account? Head to the #account-recovery channel and click on the ticket reation. One of our helpful admins will then help you recover your old account.']
  message = random.choice(advert)
  return message

def online(pnum):
  title = 'Server Online'
  desc = 'I have just checked and EO2 is online!'
  info = f'There are {pnum} people online'
  return title, desc, info

def offline():
  title = 'Server Offline'
  desc = 'I have just checked and EO2 is currently offline!'
  return title, desc