import os
import discord
from dotenv import load_dotenv
from gemini import ask_gemini

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Discord bot logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content.replace("!ask", "").strip()
        reply = ask_gemini(prompt)
        await message.channel.send(reply[:2000])

client.run(os.getenv("DISCORD_BOT_TOKEN"))
