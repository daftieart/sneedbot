import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix='#')
 
@bot.event
async def on_ready():
    print ("In the wise words of sneed, blessed is the man who seeds, who allows others to feed. And let us who follow Sneed, forgive the city slickers who fear those who possess the 4 of clubs. They are lost and instead follow the degenerate path of chuck, and his globohomo tendencies.")
 
 
@bot.event
async def on_message(message):
    channel = message.channel
    if 'sneed' in message.content:
        await message.add_reaction(":sneed:912786155886477383")
    if 'SNEED' in message.content:
        await message.add_reaction(":sneed:912786155886477383")
 
 
bot.run("OTI0MzM5MDY0MTQ3MTYxMTk4.YcdH1g.M-mSqBSwg95cNgerLP0Zt70RK7w")