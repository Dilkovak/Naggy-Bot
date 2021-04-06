import time
from functionalities import coinflip


# TODO change to use Bot not client as it there is more to offer there

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         content = message.content.split()
#         if content[0] == 'Nag':
#             if 'ping' in content:
#                 print(discord.Client.latency)
#                 await message.channel.send("Pong  🏓")
#             if 'coin' in content:
#                 coin_result = coinflip()
#                 print(coin_result)
#                 if coin_result < 0.50:
#                     await message.channel.send('Hello!')
#                 else: 
#                     await message.channel.send('Hello2!')
#                 # await message.channel.send('Hello!') if (coin_result < 0.50) else await message.channel.send('Hello2!')
#                 # await message.channel.send('Hello!')
#                 # coinflip()


#     async def on_typing(self, channel, user, when):
#         print(user)