import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.message_content = True

load_dotenv('.env')
token = os.getenv("TOKEN")

bot = commands.Bot(
    command_prefix="?",
    case_insensitive=True,
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def ping(ctx):# ctxにはコマンドの実行に関する情報を持っている(打った人など)
    if ctx.author.bot:
        return
    file = os.path.basename(__file__)
    await ctx.reply(f"pong [{file}]")

bot.run(token)