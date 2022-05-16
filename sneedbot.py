import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
 
bot = commands.Bot(command_prefix='#')
 
@bot.event
async def on_ready():
    print ("In the wise words of sneed, blessed is the man who seeds, who allows others to feed. And let us who follow Sneed, forgive the city slickers who fear those who possess the 4 of clubs. They are lost and instead follow the degenerate path of chuck, and his globohomo tendencies.")
 
@bot.event
async def on_message(message):
    channel = message.channel
    content = message.content
    if 'sneed' in content.lower():
        await message.add_reaction(":sneed:912786155886477383")

@bot.command()
async def sneed(ctx):
    await ctx.send("https://static.wikia.nocookie.net/simpsons/images/1/14/Al_Sneed.png/revision/latest/scale-to-width-down/350?cb=20210430000431")
 
token = "your Token here"
bot.run(token)
