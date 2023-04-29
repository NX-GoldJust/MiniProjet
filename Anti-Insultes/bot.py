import discord
from discord.ext import commands

bot = commands.Bot("!", intents=discord.Intents.all())

mot_interdit = ["tg", "nique", 'ta mère', 'ta mere', 'enculé', "encule", 'pd', 'gay', "con", 'connard', "pute", 'saloppe', "salope"]



@bot.event
async def on_message(msg: discord.Message):
    m = msg.content
    all_word = m.split(" ")
    dedans = False
    for mot in all_word:
        for interdit in mot_interdit:
            if mot == interdit:
                dedans = True
    await msg.delete()
    await msg.channel.send(f"Surveille ton langage {msg.author.mention}")

bot.run('TOKEN')