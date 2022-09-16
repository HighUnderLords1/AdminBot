import discord
from discord.ext import commands

class ManageMembers(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self, ):
    pass

  # Commands
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    """ || Kicks a member, Takes in a mention || """
    try:
        await member.kick(reason=reason)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    """ || Bans a user, Takes in a member mention || """
    try:
        await member.ban(reason=reason)
        await ctx.send("banned "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the ban members permission!")

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    """ || Unbans a member, Takes in member full username along with discriminator after command || """
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for banned_entry in banned_users:
      user = banned_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
        return

def setup(client):
  client.add_cog(ManageMembers(client))