from config import TOKEN
from client import MyClient
import discord

def main():
    client = MyClient()
    client.run(TOKEN)

if __name__ == '__main__':
    main()