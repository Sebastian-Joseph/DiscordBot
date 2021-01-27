import discord

blacklisted = [#insert profanity or any blacklisted words here]

TOKEN = #insert token here

client = discord.Client()

@client.event
async def on_message(message):
    await client.process_commands(message)

for i in blacklisted:
    for i in message.content:
        await message.channel.send("No cursing on this Christian server")
        await message.channel.purge(limit=1)

client.run('TOKEN')