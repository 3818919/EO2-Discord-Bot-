import configparser
import random

#Define CinfOg
def read_config():
    config = configparser.ConfigParser()
    config.read('api/advertising/ads.ini')
    return config

################################
#### DEBUG Related Settings ####
################################

#Define Discord Variables
def Ads():
  config = read_config()
  play = str(config['Adverts']['play'])
  donate = str(config['Adverts']['donate'])
  online = str(config['Adverts']['online'])
  #name = str(config['Adverts']['name']) #Uncomment to add more adverts/messages
  
  adverts = [play, donate, online] #Dont forget to return the new adverts
  advert = random.choice(adverts) #Adverts will be chosen at random from ads.ini
  return advert