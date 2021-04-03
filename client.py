import discord
from functionalities import coinflip

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        content = message.content.split()
        print(content)
        if content[0] == 'Nag':
            if 'flip' in content:
                coinflip()


    async def on_typing(self, channel, user, when):
        print(user)