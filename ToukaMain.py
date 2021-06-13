import os
import discord
import random

import keepAlive
import getPrices
import getBurns
import getFlirt

from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



bot = commands.Bot(command_prefix='!')
@bot.command(name='99')
async def nine_nine(ctx, action: str, person: str):

    if action.lower()=="burn":
        response = getBurns.burn(person)

    elif action.lower()=="flirt":
        response = getFlirt.flirt(person)

    elif action.lower()=="show":
        response = getPrices.showPrice(person)

    else:
        response = "No such command, try again!"
    
    await ctx.send(response)

keepAlive.keep_alive()

bot.run(TOKEN)

