import os
from cogs.moderacion import Moderacion
import discord
from discord.ext import commands
import asyncio

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f':ping_pong: Pong!\nMi latencia es de {(round(self.client.latency * 1000))}ms')

    @commands.command()
    async def clean(self,ctx, cantidad:int = 5):
        await ctx.channel.purge(limit=cantidad + 1)
        
def setup(client):
    client.add_cog(Utils(client))
