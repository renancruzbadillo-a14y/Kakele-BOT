import discord, json
from discord.ext import commands, tasks
import config
from ranking import atualizar_ranking
from events import buscar_eventos
from rank_image import criar_imagem_ranking
from calc import calcular_xp

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    atualizar.start()
    eventos.start()
    print("🟢 Bot online!")

# Atualizar ranking todo dia automaticamente
@tasks.loop(hours=24)
async def atualizar():
    await atualizar_ranking(config.SERVER)

# 🔹 Ranking (imagem TOP 50)
@bot.command()
async def ranking(ctx, tipo="level"):
    with open("data/ranking.json", encoding="utf-8") as f:
        data = json.load(f)

    imagem = criar_imagem_ranking(data, tipo.upper())
    await ctx.send(file=discord.File(imagem))

# 🔹 Player (stats resumidos)
@bot.command()
async def player(ctx, nick):
    embed = discord.Embed(
        title=f"🎮 {nick}",
        description="Stats do jogador",
        color=0x8e44ad
    )
    embed.add_field(name="Nível", value="?", inline=True)
    embed.add_field(name="Ataque", value="?", inline=True)
    embed.add_field(name="Defesa", value="?", inline=True)
    embed.add_field(name="Magia", value="?", inline=True)
    embed.add_field(name="Armadura", value="?", inline=True)
    embed.add_field(name="Pets", value="?", inline=False)

    await ctx.send(embed=embed)

# 🔹 Calcular XP entre níveis
@bot.command()
async def calcxp(ctx, n1: int, n2: int):
    tabela = {}  # futuramente preencher com tabela real de XP
    xp = calcular_xp(n1, n2, tabela)
    await ctx.send(f"📈 XP necessária do nível {n1} ao {n2}: **{xp}**")

# 🔹 Checar eventos (estrutura pronta)
@tasks.loop(minutes=30)
async def eventos():
    data = await buscar_eventos(config.SERVER)
    if data:
        canal = bot.get_channel(config.EVENT_CHANNEL_ID)
        for event in data.get("events", []):
            await canal.send(f"⚡ Evento ativo: {event['name']}")

bot.run(config.TOKEN)
