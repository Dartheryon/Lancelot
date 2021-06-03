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
    myID = os.getenv("myID")
    dID = os.getenv("dID")
    aramID = os.getenv("aramID")
    crysID = os.getenv("crysID")

    @commands.Cog.listener()
    async def on_message(self,ctx):
        if ctx.author == self.client.user:
            return
        author = ctx.author
        content = ctx.content
        contentLow = content.lower()
        if author.id == int(self.myID) and "hola lancelot" in contentLow:
            await ctx.channel.send('Hola poderoso '+author.mention+'! Gracias por crearme! :metal:')
        
        elif author.id == int(self.aramID) and "hola lancelot" in contentLow:
            await ctx.channel.send('Hola Grand Master del ajedrez, '+author.mention)
        
        elif author.id == int(self.crysID) and "hola lancelot" in contentLow:
            await ctx.channel.send('Hola '+author.mention+', bella creación del universo :crys2:')

        elif ("hola bebés" in contentLow) or ("hola bebes" in contentLow) or ("hola lancelot" in contentLow):
            print('entró!')
            if author.id == int(self.dID):
                await ctx.channel.send('Llegó la owner más **inteligente y hermosa** de todo Discord! Hola '+author.mention+ '! Soy tu simp, digo tu bot! Te amoooooo! ❤')


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
        
def setup(client):
    client.add_cog(Fun(client))