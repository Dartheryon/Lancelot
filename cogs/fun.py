import os
from cogs.moderacion import Moderacion
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    myID = int(os.getenv("myID"))
    dID = int(os.getenv("dID"))
    aramID = int(os.getenv("aramID"))
    crysID = int(os.getenv("crysID"))
    camiID = int(os.getenv("camiID"))

    @commands.Cog.listener()
    async def on_message(self,ctx):
        if ctx.author == self.client.user:
            return
        author = ctx.author
        content = ctx.content
        contentLow = content.lower()
        SaludosporID =[self.myID,self.dID,self.aramID,self.crysID,self.camiID]
        #Saludos personalizados
        if contentLow == 'f':
            f_embed = discord.Embed(colour = 0x2f3136)
            f_embed.set_image(url='https://raw.githubusercontent.com/Dartheryon/Lancelot/master/images/F.jpg')
            await ctx.channel.send(embed=f_embed)
        elif "hola lancelot" in contentLow:
            if author.id not in SaludosporID:
                await ctx.channel.send('Hola '+author.mention+'! Te deseo que tengas un gran día! 🙃')
            elif author.id == self.myID:
<<<<<<< HEAD
                await ctx.channel.send('Hola poderoso '+author.mention+'! Gracias por crearme! :metal:')
            elif author.id == int(self.aramID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola Grand Master del ajedrez, '+author.mention)
            elif author.id == int(self.crysID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola '+author.mention+', bella creación del universo!')
=======
                await ctx.channel.send('Hola poderoso '+author.mention+'! Gracias por crearme! <:crys2:846388711637254205> :metal:')
            elif author.id == int(self.aramID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola Grand Master del ajedrez, '+author.mention)
            elif author.id == int(self.crysID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola '+author.mention+' <:crys2:846388711637254205>, bella creación del universo!')
>>>>>>> mutaciones
            elif author.id == int(self.camiID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola '+author.mention+', mi creador me dice que eres el mejor sobrino del mundo! :metal:')
            elif author.id == int(self.dID):
                await ctx.channel.send('Llegó la owner más **inteligente y hermosa** de todo Discord! Hola '+author.mention+ '! Soy tu simp, digo tu bot! Te amoooooo! ❤')

        if ("hola bebés" in contentLow) or ("hola bebes" in contentLow):
            if author.id == int(self.dID):
                await ctx.channel.send('Llegó la owner más **inteligente y hermosa** de todo Discord! Hola '+author.mention+ '! Soy tu simp, digo tu bot! Te amoooooo! ❤')
        #Fin Saludos personalizados

    @commands.command(aliases=['oráculo'])
    async def oraculo(self, ctx, *, pregunta):
        respuestas = ['Es cierto.',
                'Sin lugar a dudas es así.',
                'Sin duda.',
                'Sí, definitivamente.',
                'Puedes confiar en ello.',
                'Como yo lo veo, sí.',
                'Es lo más probable.',
                'Hay buenas posibilidades de que ocurra.',
                'Sí.',
                'Las señales apuntan a que sí.',
                'Me confundí, intenta otra vez.',
                'Pregunta de nuevo más tarde.',
                'Mejor no te lo digo por ahora.',
                'No se puede predecir ahora.',
                'Concéntrate y pregunta otra vez.',
                'No cuentes con eso',
                'Mi respuesta es no.',
                'Mis fuentes dicen que no.',
                'Eso no se ve bien en el futuro',
                'Muy dudoso.']
        await ctx.send(f'Pregunta: {pregunta}\nRespuesta: {random.choice(respuestas)}')

    @commands.command()
    async def hola(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send('Menciona un usuario')
        else:
            await ctx.send(f'Hola {member.mention}! Eres increible!! Espero verte más seguido por acá 🙃')


def setup(client):
    client.add_cog(Fun(client))