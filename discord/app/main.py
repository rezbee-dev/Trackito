# This example requires the 'message_content' intent.

import discord
import asyncio
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.content.startswith('!time'):
            res = requests.get("http://localhost:8000/time")
            time = res.json()
            await message.reply(time["time"], mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)