# Setup #
All details specific to the server can be changed in config.ini, it was setup as such so that in the event of the main network's IP changing or projects domain's change. <br>

Main bot code found in **main.py**, commands are inside of the **cogs** directory. Functions such as scraping websites or server pings are in the **api** directory.<br>

Bot is using the [Disnake](https://docs.disnake.dev/en/stable/) library to connect to the Discord API.

# Config.ini #
Config.ini contains the bot settings, tweaking variables is best done within the config.ini file.

# Ads.ini #
Ads.ini contains the bot's auto messages, if you want to add more messages remember to also adjust the settings.ini in the Advertising folder. Ads are currently disabled in the config.ini file.

## Connecting config.ini ##
Connection to the config.ini variables are done inside config > config.py, there are also some additional functions to clear up space in the cogs.

# Commands #
Commands have been configured to slash commands or "Interactions". Current commands are /toplist, /online, /play & /donate.

## Toplist ##
This command uses webscraping of the endlessonline2.com website to obtain a list of players & their levels then format's it in a way discord can understand.
```
/toplist - Displays a list of the top 100 players in EO2
```

## Online ##
This command used webscraping of the EOSource & EOServ SLN to obtain a list of current online players. It then formats this information in a way discord can understand.
```
/online - Displays a list of online players
```

## Play ##
This command used webscraping of the EO2 website to obtain the latest download link. It then formats this information in a way discord can understand.
```
/play - Scrapes the EO2 website for the latest download link & provides it in an embed
```

## Donate ##
This command used webscraping of the EO2 website to obtain the latest donate link. It then formats this information in a way discord can understand.
```
/donate - Displays an embed linked to the EO donate page
```


# Functions inside config.ini #
Bot settings can be changed via the config.ini file, the config folder assigns those values to functions for later use. Follow the below general guide for these connections when adding additional functionality.

```
import config
```

# Functions inside api #
The "api" directory handles functions for web scraping, socket ping & api connectivity. api.py contains connections to a web based api or web scraping whereas server.py contains socket functions to ping to game server.

```
from api import api, server
```

# Dependencies #
```
python = ">=3.8.0,<3.9"
numpy = "^1.22.2"
replit = "^3.2.4"
Flask = "^2.2.0"
bs4 = "^0.0.1"
pandas = "^1.4.3"
disnake = "^2.5.2"
lxml = "^4.9.1"
```
