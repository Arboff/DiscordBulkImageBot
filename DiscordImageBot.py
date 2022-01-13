import discord
import os
 
count = 0
link = ''          #OPTIONAL: You can add anything to be send to the channel after the images are done sending, EG Invite link, socials, etc.

path = ''          #REQUIRED: Add directory to your image folders path on your local machine.


directory = os.fsencode(path)
 
TOKEN = ''      #Bot Token goes here. See Discord Developer Portal for more info.
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('Connected. Listening for !dib')     #If all is working, this message should be showing in your console. The prefix is "!dib". 
 
 
@client.event
async def on_message(message, count=0):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    #print(f'{username}: {user_message} ({channel})')    #Uncomment if you want the bot to log all messages in the console.
 
 
 
    if message.author == client.user:                   #Avoid infinite loop. DO NOT REMOVE.
        return
 
    if user_message.lower() == '!dib':                  #Upon receiving command "!dib".
        for files in os.listdir(directory):
            filename = os.fsdecode(files)
            if os.path.getsize(path + filename) < 10000000:       #If file is >10mb, it gets skipped and logged in Console due to Discord limitations.
                try:
                    await message.channel.send(file=discord.File(path + filename))
                    print(f'{filename} uploaded to: ({channel}).')
                    count += 1
                except:
                    print('Exception thrown')
            else:
                print('File size exceeds 10 000 000 bytes. :' + filename)
 
        await message.channel.send(link)
        #print(f'Sucessfully uploaded {count} files.')   Final log. Uncomments if you want to get log in console of how many files were transfered.
        
 
 
 
client.run(TOKEN) #initialization.
