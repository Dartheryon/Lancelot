import asyncio
import discord
from discord.ext import commands
import asyncio

class Moderacion(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot iniciado como {0.user}'.format(self.client))

    #Formato de tiempo para muteo temporal: 1d, 20s, 30m, etc..
    @commands.command(aliases=[''])
    @commands.has_permissions(manage_messages = True)
    async def automute(self, ctx, member: discord.Member = None, time = None, *, reason = None):
        if not member:
            await ctx.send('Menciona un usuario')
        elif not time:
            await ctx.send('define una cantidad de tiempo!')
        else:
            if not reason:
                reason = 'No especificada.'
            #Manipulación del tiempo:
            try:
                seconds = time[:-1] #Obtiene el número del argumento time, empieza en -1
                duration = time[-1] #Obtiene la manipulación temporal: s, m, h, d
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    await ctx.send("Formato de tiempo inválido")
                    return
            except Exception as e:
                print(e)
                await ctx.send('Formato de tiempo inválido')
                return
            guild = ctx.guild
            Muted = discord.utils.get(guild.roles, name="Muted")
            if not Muted:
                Muted = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permisions(Muted, speak = False, send_messages = False, read_message_history = True, read_messages = True)
            await member.add_roles(Muted, reason = reason)
            readableHex = int(hex(202225), 0)

            muted_embed = discord.Embed(title = 'Usuario Silenciado', colour = 0x2f3136, description = f"{member.mention} fue silenciado por {time}. Razón: {reason}")
            await ctx.channel.send(embed=muted_embed)
            await asyncio.sleep(int(seconds))
            await member.remove_roles(Muted)
            unmute_embed = discord.Embed(title="Silencio terminado!", colour = 0x2f3136, description=f'{self.client.user.mention} silenció a {member.mention} por: compartir enlaces no autorizados. Tiempo de sanción: {time}')
            await ctx.channel.send(embed=unmute_embed)

    @commands.Cog.listener()
    async def on_message(self,ctx):
        if ctx.author == self.client.user:
            return
        author = ctx.author
        content = ctx.content
        if 'https://discord.gg/' in content:
            await self.automute(ctx, ctx.author, '30m', reason='Está prohibido compartir enlaces de invitación!')
            await ctx.delete()
            await self.client.process_commands(ctx)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *, razon = None):
        if not member:
            await ctx.send('Menciona un usuario')
        else:
            await member.kick(reason = razon)
            kick_embed = discord.Embed(title="Usuario expulsado!", description=f'{ctx.author.mention} expulsó a {member.mention} por {razon}')
            await ctx.send(embed=kick_embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, razon = None):
        if not member:
            await ctx.send('Menciona un usuario')
        else:
            await member.ban(reason = razon)
            ban_embed = discord.Embed(title="Usuario Baneado!", description=f'{ctx.author.mention} baneó a {member.mention} por {razon}')
            await ctx.send(embed=ban_embed)

    #Formato de tiempo para muteo temporal: 1d, 20s, 30m, etc..
    @commands.command(aliases=['tempmute'])
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, member: discord.Member = None, time = None, *, reason = None):
        if not member:
            await ctx.send('Menciona un usuario')
        elif not time:
            await ctx.send('Define una cantidad de tiempo!')
        else:
            if not reason:
                reason = 'No especificada.'
            #Manipulación del tiempo:
            try:
                seconds = time[:-1] #Obtiene el número del argumento time, empieza en -1
                duration = time[-1] #Obtiene la manipulación temporal: s, m, h, d
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    await self.ctx.send("Formato de tiempo inválido")
                    return
            except Exception as e:
                print(e)
                await self.ctx.send('Formato de tiempo inválido')
                return
            guild = ctx.guild
            Muted = discord.utils.get(guild.roles, name="Muted")
            if not Muted:
                Muted = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permisions(Muted, speak = False, send_messages = False, read_message_history = True, read_messages = True)
            await member.add_roles(Muted, reason = reason)
            muted_embed = discord.Embed(title = 'Usuario Silenciado', description = f"{member.mention} fue silenciado por {ctx.author.mention}. esta cantidad de tiempo: {time}. Razón: {reason}")
            await ctx.send(embed = muted_embed)
            await asyncio.sleep(int(seconds))
            await member.remove_roles(Muted)
            unmute_embed = discord.Embed(title="Silencio terminado!", description=f'{ctx.author.mention} silenció a {member.mention} por {reason} esta cantidad de tiempo: {time}')
            await ctx.send(embed=unmute_embed)

def setup(client):
    client.add_cog(Moderacion(client))