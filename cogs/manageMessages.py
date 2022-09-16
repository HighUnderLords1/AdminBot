import discord
from discord.ext import commands

class ManageMessages(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self, ):
    pass

  # Commands
  @commands.command(aliases=['cls'])
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount=5):
    """ || Clear the channel past messages up to amount specified after command || """
    await ctx.channel.purge(limit=amount+1)
    return

  @commands.command(aliases=['msg'])
  @commands.has_permissions(send_messages=True)
  async def message(self, ctx, *, message):
    """ || Simply sends a message in the same channel that the command was sent in || """
    await ctx.channel.purge(limit=1)
    await ctx.send(message)
    return

def setup(client):
  client.add_cog(ManageMessages(client))