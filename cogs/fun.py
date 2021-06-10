import os
from cogs.moderacion import Moderacion
from cogs.utils import Utils
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

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
        
        if contentLow == 'Messirve' or contentLow == 'messirve':
            f_embed = discord.Embed(colour = 0x2f3136)
            f_embed.set_image(url='https://raw.githubusercontent.com/Dartheryon/Lancelot/master/images/messirve.png')
            await ctx.channel.send(embed=f_embed)
        if "Échale un vistazo en DIS" in content:
            print('BUMP')
            await ctx.channel.send("Les avisaré cuando sea hora de otro bump!")
            await asyncio.sleep(120*60)
            bumped_embed = discord.Embed(title="Hora de otro bump!", description=f'Ya pueden bumpear de nuevo el servidor :metal:')
            await ctx.channel.send(embed=bumped_embed)
        if contentLow == 'f':
            f_embed = discord.Embed(colour = 0x2f3136)
            f_embed.set_image(url='https://media1.tenor.com/images/a14d9b4e9a47f64890af0434a45b0388/tenor.gif')
            await ctx.channel.send(embed=f_embed)
        elif "hola lancelot" in contentLow:
            if author.id not in SaludosporID:
                await ctx.channel.send('Hola '+author.mention+'! Te deseo que tengas un gran día! 🙃')
            elif author.id == self.myID:
                await ctx.channel.send('Hola poderoso '+author.mention+'! Gracias por crearme!:metal:')
            elif author.id == int(self.aramID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola Grand Master del ajedrez, '+author.mention)
            elif author.id == int(self.crysID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola '+author.mention+' <:Crys:831029669616287784>, bella creación del universo! <:crys2:846388711637254205>')
            elif author.id == int(self.camiID) and "hola lancelot" in contentLow:
                await ctx.channel.send('Hola '+author.mention+', mi creador me dice que eres el mejor sobrino del mundo! :metal:')
            elif author.id == int(self.dID):
                await ctx.channel.send('Llegó la owner más **inteligente y hermosa** de todo Discord! <:stich_hearts:847701255588675595> Hola '+author.mention+ '!')

        if ("hola bebés" in contentLow) or ("hola bebes" in contentLow):
            if author.id == int(self.dID):
                await ctx.channel.send('Llegó la owner más **inteligente y hermosa** de todo Discord! <:stich_hearts:847701255588675595> Hola '+author.mention+ '!')
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