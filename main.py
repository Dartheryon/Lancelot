import asyncio
import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '--')

@client.event
async def on_ready():
    print('Bot iniciado como {0.user}'.format(client))


@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    author = ctx.author
    nick = author.name
    content = ctx.content

    if 'https://discord.gg/' in content:
        print('link de invitación prohibido')
        await ctx.delete()
        await automute(ctx, ctx.author, '60s', reason='Está prohibido compartir enlaces de invitación!')
    await client.process_commands(ctx)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! mi latencia es de {(round(client.latency * 1000))}ms')

@client.command()
async def hola(ctx):
    nickname = ctx.author.name
    await ctx.channel.send(f'Hola {nickname}!  Soy Lancelot. Un gusto saludarte')

@client.command(aliases =['8ball','oraculo','oráculo']) 

async def _8ball(ctx, *, pregunta):
    respuestas = ['Es cierto.',
                'Es decididamente así.',
                'Sin duda.',
                'Sí definitivamente.',
                'Puedes confiar en ello.',
                'Como yo lo veo, sí.',
                'Más probable.',
                'Hay buenas posibilidades.',
                'Sí.',
                'Las señales apuntan a que sí.',
                'Respuesta confusa, intenta otra vez.',
                'Pregunta de nuevo más tarde.',
                'Mejor no decirte ahora.',
                'No se puede predecir ahora.',
                'Concéntrate y pregunta otra vez.',
                'No cuentes con eso',
                'Mi respuesta es no.',
                'Mis fuentes dicen que no.',
                'Eso no se ve bien en el futuro',
                'Muy dudoso.']
    await ctx.send(f'Pregunta: {pregunta}\nRespuesta: {random.choice(respuestas)}')

@client.command()
async def clear(ctx, cantidad = 5):
    await ctx.channel.purge(limit=cantidad + 1)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, razon = None):
    await member.kick(reason = razon)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, razon = None):
    await member.ban(reason = razon)

#Formato de tiempo para muteo temporal: 1d, 20s, 30m, etc..
@client.command(aliases=['tempmute'])
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member = None, time = None, *, reason = None):
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
        muted_embed = discord.Embed(title = 'Usuario Silenciado', description = f"{member.mention} fue silenciado por {ctx.author.mention}. esta cantidad de tiempo: {time}. Razón: {reason}")
        await ctx.send(embed = muted_embed)
        await asyncio.sleep(int(seconds))
        await member.remove_roles(Muted)
        unmute_embed = discord.Embed(title="Silencio terminado!", description=f'{ctx.author.mention} silenció a {member.mention} por {reason} esta cantidad de tiempo: {time}')
        await ctx.send(embed=unmute_embed)


#Formato de tiempo para muteo temporal: 1d, 20s, 30m, etc..
@client.command(aliases=['botautomute'])
@commands.has_permissions(manage_messages = True)
async def automute(ctx, member: discord.Member = None, time = None, *, reason = None):
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
        #await ctx.send(embed = muted_embed)
        await asyncio.sleep(int(seconds))
        await member.remove_roles(Muted)
        unmute_embed = discord.Embed(title="Silencio terminado!", colour = 0x2f3136, description=f'{client.user} silenció a {member.mention} por: compartir enlaces no autorizados. Tiempo de sanción: {time}')
        await ctx.channel.send(embed=unmute_embed)


Token = os.getenv("BOT_TKN")
client.run(Token)
