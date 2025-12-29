# Bot discord par manu_8001
# Copyright (c) 2025 tous droits réservés

# Importation des bibliothèques
import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

class threads(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(threads(bot))
    print('Cog threads chargé avec succès')