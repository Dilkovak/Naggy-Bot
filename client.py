
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print(type(message))
        print(message)
        # print('Message from {0.author}: {0.content}'.format(message))
        if 'nag ' in message.content:
            print(message.content)
    # async def responde(self, )