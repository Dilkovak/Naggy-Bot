import time
import psutil
import platform
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

    @commands.command()
    async def system_info(self, ctx):
        memory = psutil.virtual_memory()
        cpu_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
        embedVar = discord.Embed(title="Naggy's System Information 🖥", color=0x00ff00)
        embedVar.add_field(name="Operating System", value=platform.system(), inline=False)
        embedVar.add_field(name="Processor", value=platform.processor(), inline=True)
        embedVar.add_field(name="CPU Usage", value=f"{round(sum(cpu_load) / len(cpu_load), 2)}%", inline=True)
        embedVar.add_field(name="Memory", value="------------------------------------------------------------", inline=False)
        embedVar.add_field(name="Total", value=f"{round(memory.total / 1024 / 1024, 2)} MB", inline=True)
        embedVar.add_field(name="Available", value=f"{round(memory.available / 1024 / 1024, 2)} MB", inline=True)
        embedVar.add_field(name="Available %", value=f"{100 - memory.percent}%", inline=True)
        await ctx.send(embed=embedVar)

    # plaftorm.processor() for processor
    # platform.platform() os info (imight not need processor)
    # platform.system() shows linux
    # psutil for ram usage (cpu usage?)
    # cpu_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    # sum(cpu_load) / len(cpu_load)