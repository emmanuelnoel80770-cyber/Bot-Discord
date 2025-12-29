# Bot discord par manu_8001
# Copyright (c) 2025 tous droits réservés

# Importation des bibliothèques
import os
import discord

from discord.ext import commands

class SystemMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # Fonction qui affiche un message de validation.
    # Paramètres: self = object
    #             ctx = array(title, message, guild_id, channel_id, embed)
    async def ValidMesage(self, ctx):
        

