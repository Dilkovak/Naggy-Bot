from config import TOKEN
from discord.ext import commands
from client import BotUtility

def main():
    prefix = "Nag "
    bot = commands.Bot(command_prefix=prefix)
    bot.add_cog(BotUtility(bot))
    bot.run(TOKEN)  # Where 'TOKEN' is your bot token

if __name__ == '__main__':
    main()

# bot.run(TOKEN)  # Where 'TOKEN' is your bot token