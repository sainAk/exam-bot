import json
import os

import discord
from discord.ext import commands

emojis = ["1⃣", "2⃣", "3⃣", "4⃣"]
TOKEN = os.getenv("TOKEN")

client = discord.Client()
bot = commands.Bot(command_prefix="$")


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello! " + message.author.name)

    if message.content.startswith("$fmt"):
        try:
            data = json.loads(message.content[5:])
            for question in data["ques"]:
                mm = f"```{question['question']}"
                for i, opt in enumerate(question["options"]):
                    mm += f"\n{i+1}. {opt}"
                mm += "```"
                msg = await message.channel.send(mm)
                for emoji in emojis:
                    await msg.add_reaction(emoji)
        except:
            await message.channel.send("error")


bot.run(TOKEN)