import scrapy
import filecmp
import shutil
import os
import json
import discord

class Nuuvem(scrapy.Spider):
    name = 'nuuvem'
    start_urls = ['https://www.nuuvem.com/catalog/price/promo/sort/bestselling/sort-mode/desc']

    def parse(self, response):
        for item in response.css('.product__unavailable'):
            yield {'name': item.css('::attr(data-track-product-name)').get(),'link': item.css('::attr(data-track-product-url)').get(), 'price': item.css('::attr(data-track-product-price)').get()}

def anyNewGame():
    if filecmp.cmp(os.getcwd()+'/scrappers/nuuvem.json', os.getcwd()+'/scrappers/bkp_nuuvem.json') == False:
        shutil.copyfile(os.getcwd()+'/scrappers/nuuvem.json', os.getcwd()+'/scrappers/bkp_nuuvem.json')
        return True
    return False

async def notifyChannel(channel):
    try:
        if anyNewGame() == True:
            with open(os.getcwd()+'/scrappers/nuuvem.json') as f:
                games = json.load(f)

            embedVar = discord.Embed(title="Promoções de jogos", color=0x00ff00)

            for game in games:
                gameName = game['name']+" ("+game['price']+")"
                gameLink = "[Entrar no link]("+game['link']+")"
                embedVar.add_field(name=gameName, value=gameLink, inline=True)

            await channel.send(embed=embedVar)
        else:
            await channel.send('Não tem jogo arrombado')
    except Error:
        print(Error)
    
