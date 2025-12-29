# Bot discord par manu_8001
# Copyright (c) 2025 tous droits réservés

# Importation des bibliothèques
import os
import discord
from discord.ext import commands

class system_message(commands.Cog):
    def __init__(self, bot):
       self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       print(f'Connecté en tant que {self.bot.user}')


async def setup(bot):
   await bot.add_cog(system_message(bot))
   print('Cog system_message chargé avec succès')

