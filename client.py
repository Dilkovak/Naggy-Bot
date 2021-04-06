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
        await ctx.send("testing")

    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        await ctx.send(latency)