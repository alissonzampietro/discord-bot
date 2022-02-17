import os
from dotenv import load_dotenv
import discord
load_dotenv()
client = discord.Client();

# Modules
from lib.troll_voice import runVoice 
from lib.nuuvem_sales import runScrap 


# execution
runVoice(client)
runScrap(client)

client.run(os.getenv('DISCORD_TOKEN'))