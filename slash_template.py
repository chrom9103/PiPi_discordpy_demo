import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv('.env')
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.tree.command(name="ping", description="Check if bot is alive")
async def ping(ctx: discord.Interaction):
    if ctx.user.bot:
        return
    file = os.path.basename(__file__)
    await ctx.response.send_message(f"pong [{file}]")

bot.run(token)