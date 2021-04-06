from config import TOKEN
from discord.ext import commands
prefix = "?"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
      print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

def main():
    bot.run(TOKEN)  # Where 'TOKEN' is your bot token

if __name__ == '__main__':
    main()

# bot.run(TOKEN)  # Where 'TOKEN' is your bot token