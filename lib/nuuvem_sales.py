import os
from scrappers.nuuvem import notifyChannel


def runScrap(client):
    @client.event
    async def on_message(message):
        print(message.channel.id)
        if message.author == client.user:
            return
        if message.content.startswith(os.getenv('MESSAGE_TRIGGER_NUUVEM')):
            await notifyChannel(message.channel)