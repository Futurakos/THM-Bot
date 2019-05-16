# TryHackMe Discord Bot
# Created by DarkStar7471 aka J0n
import discord
from discord.ext import commands

inputFile = "token.txt"
workingFile = open(inputFile)
TOKEN = workingFile.readline()

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)