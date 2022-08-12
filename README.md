# Setup #
All details specific to the server can be changed in config.ini, it was setup as such so that in the event of the main network's IP changing or projects domain's change. <br><br>

This bot was built inside of the replit.com platform, the bot's "Token" is stored inside of private database within replit. Additionally some folders displayed inside of github pertain directly to that platform.<br><br>

Bot is uring the [Disnake](https://docs.disnake.dev/en/stable/) library to connect to the Discord API.

# Config.ini #
Config.ini has 5 sections: DiscordServer for discord server configs, Advert for automated message configs, ServerSettings for game server settings, Website for game related urls, StatusAlerts for admin alerts for when the game goes offline.

## Connecting config.ini ##
Connection to the config.ini variables are done inside config > config.py, there are also some additional functions to clear up space in the cogs.

# Commands #
Commands have been configured to slash commands or "Interactions". Current commands are /toplist & /online.

## Toplist ##
This command uses webscraping of the endlessonline2.com website to obtain a list of players & their levels then format's it in a way discord can understand.
```
/toplist - Displays a list of the top 100 players in EO2
```

## Online ##
This command used webscraping of the EOSource & EOServ SLN to obtain a list of current online players. It then formats this information in a way discord can understand.
```
/online
```


# Functions inside config.ini #
Bot settings can be changed via the config.ini file, the config folder assigns those values to functions for later use. Follow the below general guide for these connections when adding additional functionality.

```
from config import config, server
```

## Advertising ##
```
ServerID: ID of the discord server, needed for discord's API
Advertising: Are times messages enabled (bool)
Channel: The channel you want the discord bot to post messages.
```
> ServerID, advertising, channel = config.Discord()

## Game Server ##
```
IP: EO2 Server IP
Port: EO2 Server Port
Retry : How many times to retry a ping when checking status
Timeout: How long before server ping timeout
```
> ip, port, retry, timeout = config.Server()

## Data Connection ##
```
Domain: Main website domain found in config.ini
Ranks: Domain to game toplists found in config.ini
Discord: Link to discord invite
Download: Link to download client
Online: URL of EOSource SLN found in config.ini
Backup: URL to EOServ as a backup, found in config.ini
```
> domain, ranks, discord, download, online, backup = config.API()

## Bot Alerts ##
```
Alert_Check: If bot alerts are enabled
Alert_Channel: Channel the bot posts admin alerts to
Alert_Admin: The admin who the bot will ping if the game goes offline
```
> alert_check, alert_channel, alert_admin = config.Alerts()
