import os
import datetime
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.voteChannelID = int(os.getenv('DISCORD_VOTE_CHANNEL_ID'))
        self.voteChannel = None
        self.voteResponseChoice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    def voteChannelInit(self, ctx):
        if self.voteChannel is None:
            self.voteChannel = ctx.guild.get_channel(self.voteChannelID)

    def getVoteByStringContains(self, pattern):
        self.voteChannelInit(ctx)
        messages = await self.voteChannel.history(limit=50).flatten()
        for message in messages:
            if pattern in message.content:
                return message
        return None

    def votesMsg(self, author, createTime, endTime, voteNbr):
        ret = "``` Vote numéro " + voteNbr + "\n"
        ret += "*Soumis par " + author + ", le " + createTime + ".*\n"
        ret += "*Le vote prendra fin le " + endTime + ".*\n"
        ret += "__________________________________________" + "\n"
        ret += text + "```"
        return ret


    @commands.command()
    async def vote(self, ctx, voteNbr, endTime, text):
        """Crée un vote. usage: vote[id][date_de_fin][texte]"""
        self.voteChannelInit(ctx)
        ret = voteMsg(ctx.author.nick, ctx.message.created_at.strftime("%d/%m/%y à %H:%M"), endTime, voteNbr)
        sendedMsg = await self.voteChannel.send(ret)
        await sendedMsg.add_reaction("👍")
        await sendedMsg.add_reaction("👎")
        await sendedMsg.add_reaction("🏳")

    @commands.command()
    async def voteType2(self, ctx, voteNbr, endTime, text, responseNbr):
        self.voteChannelInit(ctx)
        ret = voteMsg(ctx.author.nick, ctx.message.created_at.strftime("%d/%m/%y à %H:%M"), endTime, voteNbr)
        sendedMsg = await self.voteChannel.send(ret)
        i=0
        while i < responseNbr
            await sendedMsg.add_reaction(self.voteResponseChoice)
            i++

    @commands.command()
    async def cancelVote(self, ctx, voteNbr):
        """Anuler un vote"""
        pattern = "Vote numéro " + str(voteNbr)
        voteMessage = self.getVoteByStringContains(pattern)

        if voteMessage is not None :
            editedVoteMessage = "❌LE VOTE EST FINI❌\n" + voteMessage.content
            await voteMessage.edit(content=editedVoteMessage)
        else:
            await ctx.send(pattern + " introuvable")

    @commands.command()
    async def endVote(self, ctx, voteNbr):
        """Finir un vote: marque le message du vote comme étant un vote fini, compte les voix."""
        toFind = "Vote numéro " + str(voteNbr)
        voteMessage = self.getVoteByStringContains(toFind)

        if voteMessage is not None :
            editedVoteMessage = "❌LE VOTE EST FINI❌\n" + voteMessage.content
            await voteMessage.edit(content=editedVoteMessage)
            ret = "```Résultats du vote numéro " + voteNbr + ":\n"
            for reaction in voteMessage.reactions:
                ret += reaction.emoji + " : " + str(reaction.count - 1) + " | "
            ret += "```"
            await self.voteChannel.send(ret)
        else:
            await ctx.send(pattern + " introuvable")
