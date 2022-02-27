from scrappers.nuuvem import notifyChannel


def runScrap(client):
    @client.event
    async def on_message(message):
        print(message.channel.id)
        if message.author == client.user:
            return
        if message.content.startswith('tem jogo?'):
            await notifyChannel(message.channel)