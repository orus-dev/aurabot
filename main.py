from aura import *
from config import *
import discord
from discord import app_commands
from discord.ext import commands
import time

aura = Aura()
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(client.user)
    for guild in client.guilds:
        async for member in guild.fetch_members(limit=None):
            user = aura.get(str(member.id))
            if user==None:
                aura.add(str(member.id))
    print(await tree.sync())

@client.event
async def on_message(msg: discord.Message):
    if msg.author.bot:
        return
    user = aura.get(str(msg.author.id))
    if user==None:
        return
    if int(time.time() - user.last_earned) >= COOLDOWN_PERIOD:
        user.balance += 3
        user.last_earned = time.time()
        aura.update(user)

@client.event
async def on_member_join(member: discord.Member):
    user = aura.get(str(member.id))
    if not user:
        user = aura.add(str(member.id))
    await member.send(embed=discord.Embed(color=member.color, title='✨ Welcome to ORUS! ✨', description=f'**Aura: {user.balance}\nInvite URL: ```{INVITE+str(member.id)}```\nShare this Invite URL for +120 aura per join!**'))

@tree.command(name='aura', description='Check the amount of aura a member has')
async def get_aura(interaction: discord.Interaction, member: discord.Member = None):
    if member == None:
        member = interaction.user
    user = aura.get(str(member.id))
    embed = discord.Embed(color=member.color, title=f'{member.name}\'s Aura', description=user.to_md())
    await interaction.response.send_message(embed=embed)

@tree.command(name='send', description='Send aura to a member')
async def send(interaction: discord.Interaction, to: discord.Member, amount: int, reason: str = ""):
    user = aura.get(str(interaction.user.id))
    user_to = aura.get(str(to.id))
    if amount < 0:
        amount = -amount
        for r in interaction.user.roles:
            if str(r.id) in PUNISH_ROLES:
                if user_to.balance >= amount:
                    user_to.balance -= amount
                    user.balance += 10
                    await to.send(embed=discord.Embed(
                        color=interaction.user.color,
                        title="Punished!",
                        description=f'**By: {interaction.user.name}\nAmount: {amount}\nReason: {reason}**'
                    ))
                    await interaction.response.send_message(f'Punished! You gained 10+ aura!', ephemeral=True)
                else:
                    await interaction.response.send_message(f'Cannot punish. {to.name} only has {user_to.balance} aura!', ephemeral=True)
                return
        if user.balance >= 10:
            user.balance -= 10
        await interaction.response.send_message(f'Cannot punish. You are not a developer.{" -10 aura!" if user.balance>=10 else""}', ephemeral=True)
        aura.update(user)
        aura.update(user_to)
        return
    else:
        if user.balance >= amount:
            user.balance -= amount
            user_to.balance += amount
            await to.send(embed=discord.Embed(
                color=interaction.user.color,
                title="Aura received!",
                description=f'**From: {interaction.user.name}\nAmount: {amount}**'
            ))
            await interaction.response.send_message(f'Sent! You now have {user.balance} aura!', ephemeral=True)
            aura.update(user)
            aura.update(user_to)
        else:
            await interaction.response.send_message(f'Cannot send. You only have {user.balance} aura!', ephemeral=True)

client.run(BOT_TOKEN)