# Setup #
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
