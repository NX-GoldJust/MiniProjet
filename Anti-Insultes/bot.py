import discord
from discord.ext import commands

bot = commands.Bot("!", intents=discord.Intents.all())

mot_interdit = ["tg", "nique", 'ta mère', 'ta mere', 'enculé', "encule", 'pd', 'gay', "con", 'connard', "pute", 'saloppe', "salope"]