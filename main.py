# Bot discord par manu_8001
# Copyright (c) 2025 tous droits réservés

# Importation des bibliothèques
import os
import discord

from discord.ext import commands

# On extrait le token du bot
token = os.environ['Token_Bot_Discord']

class BotDiscord(commands.Bot):
    async def setup_hook(self):
        for extension in ['system_message', 'threads']:
            try:
                await self.load_extension(f'cogs.{extension}')
                print(f'Cog {extension} chargé avec succès')
            except Exception as e:
                print(f'Erreur lors du chargement de {extension}: {e}')

intents = discord.Intents.all()
bot = BotDiscord(command_prefix="!", intents=intents)

bot.run(token=token)