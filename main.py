import discord
from discord.ext import commands 

from dotenv import load_dotenv
import os

load_dotenv()
Discord_token = os.getenv("Discord.token")

intents = discord.Intents.all()
#                prefiso do bot
bot = commands.Bot("&", intents=intents)

# eventos

# evento do bot ligado
@bot.event
async def on_ready():
    print("boccchi começo a tocar")

# evento membro novo
@bot.event
async def on_member_join(membro:discord.member):
    canal = bot.get_channel(1482831387273724027)
    await canal.send(f"{membro.mention} entrou no servidor")

# evento mansagem no caht

#@bot.event
#async def on_message(msg:discord.message):
   #if msg.author.bot:
        #return
    # mancar o aroba do usuario
        #await msg.reply(f"{msg.author.mention}")
    #apenas responder o usuario
        #await msg.reply("por que voce mandou mansagem??")
    # mencionar o canal
        #await msg.reply(f"no canal {msg.channel.name}" )


# comandos

# responder uma mensagm
@bot.command()
async def ola(ctx:commands.context): 
    nome = ctx.author.name 
    await ctx.reply(f"ola! {nome} tudo bem?")

# reinviar uma mansagem
@bot.command()
async def falar(ctx:commands.context, *,texto): 
   await ctx.send(texto)

#
@bot.command()
async def enbed(ctx:commands.context):
    nome = ctx.author.name 
    foto_perfil = ctx.author.avatar.url

    minha_embed = discord.Embed(
    title ="bocci feliz" ,
    description ="bocchi ta fliz por que fez amigos",
    color = 0xffcbdb
    )

    minha_embed.set_author(name=nome, icon_url=foto_perfil)
    await ctx.reply(embed=minha_embed)

contador_sugestao = 0

@bot.command()
async def falar2(ctx:commands.context, *, texto):
    global contador_sugestao
    contador_sugestao += 1
    await ctx.message.delete()
    nome = ctx.author.name 
    foto_perfil = ctx.author.avatar.url

    minha_embed = discord.Embed(
    title =f"sugestão numero {contador_sugestao}# " ,
    description = texto,
    color = 0xffcbdb
    )

    minha_embed.set_author(name=nome, icon_url=foto_perfil)
    await ctx.send(embed=minha_embed)

@bot.command()
async def falar3(ctx:commands.context, *, texto):
    global contador_sugestao
    contador_sugestao += 1
    await ctx.message.delete()
    nome = ctx.author.name 
    foto_perfil = ctx.author.avatar.url

    minha_embed = discord.Embed(
    title =f"sugestão numero {contador_sugestao}# " ,
    description = texto,
    color = 0xffcbdb
    )

    minha_embed.set_author(name=nome, icon_url=foto_perfil)
    mensagem_enviada = await ctx.send(embed=minha_embed)
    await mensagem_enviada.add_reaction("⬆️")
    await mensagem_enviada.add_reaction("⬇️")



bot.run(Discord_token)