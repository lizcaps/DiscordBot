import os
import datetime
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voteChannelID = int(os.getenv('DISCORD_VOTE_CHANNEL_ID'))

    @commands.command()
    async def report(ctx, discordIdentifier, text):
        txt = text
        # report un membre. le message est:
        #   ajouté dans le salon de signalement
        #   concat dans un message du salon de signalement portant déja sur cet utilisateur

    @commands.command()
    async def ban(ctx, discordIdentifier, text):
        txt = text
        #ban un membre
        #ajoute un message dans le salon de signalement
        #   concat dans un message du salon de signalement portant déja sur cet utilisateur
        # publication d'une annonce dans le canal annonce ?


    @commands.command()
    async def kick(ctx, discordIdentifier, text):
        txt = text
        #kick un membre
        #ajoute un message dans le salon de signalement
        #   concat dans un message du salon de signalement portant déja sur cet utilisateur
