import os
from dotenv import load_dotenv
import discord


load_dotenv()

client = discord.Client();
is_channel_connected = False

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.channel)

    await message.channel.send('Vai te foder')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

async def close_connection():
    await event.disconnect

async def bomdia(member, channel):
    global is_channel_connected
    if channel != None and is_channel_connected == False:
        is_channel_connected = True
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio('bomdiaminharainha.mp3'))
        await channel.disconnect()


@client.event
async def on_voice_state_update(member, before, after):
    await bomdia(member, after.channel)


client.run(os.getenv('DISCORD_TOKEN'))