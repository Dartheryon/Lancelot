import asyncio
import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '--')

#Carga de Cogs

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

Token = os.getenv("BOT_TKN")
client.run(Token)
