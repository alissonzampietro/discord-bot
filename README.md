# Discord BOT

## Requirements
    - Docker >= 20

## How use the code:
 - Rename *.env-example* to *.env* and input the token of your discord bot in the field *DISCORD_TOKEN*
 - create directory called *audios* in the root and fill with all audios that you want to use
 - Install [docker](https://docs.docker.com/get-docker/) on your machine
 - Open your terminal in the root of the project run the command: `docker build . --tag discord-bot`
 - And after the previous command finish, run: `docker run -d -v /usr/src/app/ discord-bot:latest`
 - It's ready to use :-)


## Features:
  - Play random song when someone enter in some channel from the server :heavy_check_mark: 
  - Get games on sales from [Nuuvem](https://www.nuuvem.com/) when requested by channel member :heavy_check_mark: 
  - Notify channel automatically when there's some new game on sales available on [Nuuvem](https://www.nuuvem.com/) :heavy_multiplication_x: 


If you prefer, you can invite my bot :-)

[Add me](https://discordapp.com/oauth2/authorize?client_id=939959067915477103&scope=bot&permissions=36760640)