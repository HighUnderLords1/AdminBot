import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from webapp import keep_alive
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

keep_alive()

client = commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    game = discord.Game("the Moderator Game")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.trigger_typing()
    await ctx.send("That is not a command! ")
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.trigger_typing()
    await ctx.send("Please pass in all required arguements.")
  else:
     raise error

@client.command()
async def ping(self, ctx):
    " || Sends back !pong, Used for testing"
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

@client.command()
async def load(ctx, extension):
  """ || Do not use, This is part of the internal condition || """
  client.load_extension(f"cogs.{extension}")

async def reload(ctx, extension):
  """ || Do not use, This is part of the internal condition || """
  client.unload_extension(f"cogs.{extension}")
  client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
  """ || Do not use, This is part of the internal condition || """
  client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!