import discord
from discord.ext import commands

class ManageRoles(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    pass

  # Commands
  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def make_role(self, ctx, *, role_name : str):
    """ || Makes a role, Parameters, role name"""
    guild = ctx.guild
    await guild.create_role(name=role_name)
    await ctx.trigger_typing()
    await ctx.send(f"Role {role_name} Added!")

  @commands.command(aliases=['del_role'])
  @commands.has_permissions(manage_roles=True)
  async def delete_role(self, ctx, *, role_name : str):
    """ || Deletes roles, Parameters, role name || """
    guild = ctx.guild
    roles = await guild.fetch_roles()
    for role in roles:
      roleName = role.name
      if roleName == role_name:
        await role.delete()
        await ctx.trigger_typing()
        await ctx.send(f"Role {role_name} Deleted!")
        return
    await ctx.trigger_typing()
    await ctx.send(f'Role {role_name} not found.')

  @commands.command(aliases=['append_role'])
  @commands.has_permissions(manage_roles=True)
  async def add_role(self, ctx, role_name : str, member : discord.Member):
    """ || Adds roles to member, Parameters, role name and member mention || """
    guild = ctx.guild
    roles = await guild.fetch_roles()
    for role in roles:
      roleName = role.name
      if roleName == role_name:
        await member.add_roles(role)
        await ctx.trigger_typing()
        await ctx.send(f"Role {role_name} added to {str(member)[:-5]}!")
        return

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def has_role(self, ctx, role_name : str, member : discord.Member):
    """ || Returns if the member has the role or not, Parameters, role name and member mention || """
    names = []
    for role in member.roles:
      names.append(role.name)
    await ctx.trigger_typing()
    await ctx.send(str(role_name in names))

  @commands.command()
  @commands.has_permissions(manage_roles=True)
  async def remove_role(self, ctx, role_name : str, member : discord.Member):
    names = []
    for role in member.roles:
      names.append(role.name)
    if role_name in names:
      for role in member.roles:
        if role.name == role_name:
          await member.remove_roles(role)
          await ctx.trigger_typing()
          await ctx.send(f"Role {role_name} removed from {str(member)[:-5]}")
    else:
      await ctx.trigger_typing()
      await ctx.send(f"Member {str(member)[:-5]} does not have Role {role_name}")

def setup(client):
  client.add_cog(ManageRoles(client))