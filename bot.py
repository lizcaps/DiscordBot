import os
import datetime
import asyncio
import discord
import re
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime
from vote import Vote
from admin import Admin

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server = os.getenv('DISCORD_SERVER_NAME')
server_id = os.getenv('DISCORD_SERVER_ID')
bot = commands.Bot(command_prefix='!')

bot.add_cog(Vote(bot))
#bot.add_cog(Admin(bot))

@bot.event
async def on_ready():
    print('_______________')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('_______________')

bot.run(token)
