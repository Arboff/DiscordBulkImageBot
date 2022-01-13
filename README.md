# Discord Bulk Image Sending Bot
## Send bulk images to Discord channel.


This is a bot script that will allow you to send multiple images to Discord channel avoiding the 10 media per time limitation + Bypass for file size limitation.

## Requiremens:


- Python 3.9
- Discord.py (pip install discord)
- Discord bot with the following permissions:
-- Send Messages.
-- Send Messages in Threads.
-- Send TTS Messages.
-- Embed Links (In case you need to send a link as a footer.).
-- Attach Files.
-- Use Slash Commands.

## Features

- Bypass Discord limitation of 10 media files per Message.
- Fully automatic.
- Doesn't try to send files bigger than Discord Limitations (10mb).
- Unlimited File Count.
- No need for cloud host, works on your machine, open source, no chance for token steal.



## Installation

DIB requires [Python ](https://www.python.org/)  3.9 to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install discord
pip install os #Just in case you are missing the package for some reason.
```


## Variables

Footer # OPTIONAL #:

```sh
link = ''         #OPTIONAL: You can add anything to be send to the channel after the images are done sending, EG Invite link, socials, etc.
```

Path to Folder # REQUIRED #:

```sh
path = ''          #REQUIRED: Add directory to your image folders path on your local machine.
```

TOKEN # REQUIRED #:

```sh
TOKEN = ''      #Bot Token goes here. See Discord Developer Portal for more info.
```


Log in Console # OPTIONAL #:

```sh
#print(f'{username}: {user_message} ({channel})')    #Uncomment if you want the bot to log all messages in the console.
```

Infinite Loop Protection # REQUIRED #:

```sh
if message.author == client.user:                   #Avoid infinite loop. DO NOT REMOVE.
```

Size Limiter # REQUIRED #:

```sh
if os.path.getsize(path + filename) < 10000000:       #If file is >10mb, it gets skipped and logged in Console due to Discord limitations.
```

Final Log # OPTIONAL #:

```sh
#print(f'Sucessfully uploaded {count} files.')   Final log. Uncomments if you want to get log in console of how many files were transfered.
```
Bot Initialization # REQUIRED #:

```sh
client.run(TOKEN) #initialization.
```



## License

MIT

**Free Software, Hell Yeah!**


