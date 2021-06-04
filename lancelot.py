import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import asyncio

load_dotenv()

client = commands.Bot(command_prefix = '--')

#Carga de Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


##Cambiando la presencia cada X tiempo:

async def ch_presence():
    await client.wait_until_ready()
    tiposPresencia= ["Playing","Listening","Watching"]
    while not client.is_closed():
        accion = random.choice(tiposPresencia)
        if accion == 'Playing':
            juegos = ["quitarte a tu novia","quitarte a tu novio","MTG","CSGO",'Pokémon Esmeralda',"Genshin Impact","World of Warcraft","Bloons TD battles"]
            juego = random.choice(juegos)

            await client.change_presence(activity=discord.Game(name=juego))

        elif accion == "Listening":
            songs = ['Metallica', 'Gothic Metal', 'Metal Colombiano', 'Frank Sinatra', 'AC/DC','Therion', 'Cantar a Dandelius','Mozart','Rock Argentino']
            song = random.choice(songs)

            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = song))

        elif accion == "Watching":
            shows = ['The Boys', 'Naruto', 'Kimetsu no Yaiba ', 'Star Wars', 'como juegan contigo','Pulp Fiction', 'Invincible','crecer mi amor por Dani ❤❤' ]
            show = random.choice(shows)

            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = show))
        await asyncio.sleep(6*60)

client.loop.create_task(ch_presence())


Token = os.getenv("BOT_TKN")
client.run(Token)
