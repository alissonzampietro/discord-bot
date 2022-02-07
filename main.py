import os
import time
import random
from dotenv import load_dotenv
import discord


load_dotenv()

client = discord.Client();

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_voice_state_update(member, before, after):
    await bomdia(member, after)


def playRandomAudio(voice):
    allAudios = os.listdir("audios/")
    choice = random.choice(allAudios)
    voice.play(discord.FFmpegPCMAudio('audios/'+choice))


async def bomdia(member, event):
    try:
        if event.channel != None and member != client.user:
            voice = await event.channel.connect()
            playRandomAudio(voice)
            time.sleep(5)
            await voice.disconnect()
    except:
        print('Error: User connected twice')



client.run(os.getenv('DISCORD_TOKEN'))