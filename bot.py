import discord
from discord.ext import commands
import os
from googleapiclient.discovery import build

#! Import this
import random
intents = discord.Intents().all()
client = commands.Bot(command_prefix="$" , intents=intents)

api_key = "AIzaSyAaNQjgyawFm3ari3LvTBqjXvZkxNny-rk"


@client.event
async def on_ready():
    print("!!! Bot Is Online !!!\n")


@client.command(aliases=["picaboo"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="5522dbafa14ab4b2a", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search}) ")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


client.run("MTA4OTU3NDU0ODU5ODQ0NDIwMg.GS7dDt.q3n9GMHtZn4GGEpk0nCW1QBhqsTEb-pfr7q7XI")
