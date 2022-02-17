import os
import time
import random
import discord

def runVoice(client):
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
        audioFolder = os.getcwd()+'/audios/'
        allAudios = os.listdir(audioFolder)
        choice = random.choice(allAudios)
        voice.play(discord.FFmpegPCMAudio(audioFolder+choice))


    async def bomdia(member, event):
        print(member)
        try:
            if event.channel != None and member != client.user:
                voice = await event.channel.connect()
                playRandomAudio(voice)
                time.sleep(5)
                await voice.disconnect()
        except Error:
            print(Error)