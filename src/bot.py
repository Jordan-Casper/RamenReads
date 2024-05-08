import discord
from discord.ext import commands

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Event listener for when the bot has switched from offline to online.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to respond to a simple 'hello'
@bot.command(name='hello', help='Responds with a greeting')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

# Replace 'YOUR_BOT_TOKEN_HERE' with your bot's token
bot.run('YOUR_BOT_TOKEN_HERE')
