import time
from functionalities import coinflip
from discord.ext import commands
import discord

class BotUtility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
          print(f'We have logged in as {self.bot.user}')

    @commands.command()
    async def testing(self, ctx):
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        embedVar.set_footer(text="footer")
        await ctx.send(embed=embedVar)
        # await ctx.send("testing")

    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        await ctx.send(latency)