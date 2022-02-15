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
    if(is_avoidable_events(before, after) == False):
        await bomdia(member, after)


def is_avoidable_events(before, after):
    return any([before.self_mute,after.self_mute,before.mute,after.mute,before.deaf,after.deaf,before.self_deaf,after.self_deaf,before.self_stream,after.self_stream,before.self_video,after.self_video])


def playRandomAudio(voice):
    allAudios = os.listdir("audios/")
    choice = random.choice(allAudios)
    voice.play(discord.FFmpegPCMAudio('audios/'+choice))


async def bomdia(member, event):
    print(member)
    try:
        if event.channel != None and member != client.user:
            voice = await event.channel.connect()
            playRandomAudio(voice)
            time.sleep(5)
            await voice.disconnect()
    except:
        print('Error: User connected twice')



client.run(os.getenv('DISCORD_TOKEN'))