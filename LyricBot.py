import discord
import lyricsgenius
from discord.ext import commands

GENIUS = ""
client = commands.Bot(command_prefix="!")
TOKEN = # insert token here

@client.command()
async def search(ctx, *args):
    genius = lyricsgenius.Genius("enter genius token here")
    artist = genius.search_song(args)
    lyrics = str(artist.lyrics)
    await ctx.send(artist.lyrics[0:len(artist.lyrics) // 2])
    #sends half of lyrics due to discord character limit

client.run(TOKEN)
