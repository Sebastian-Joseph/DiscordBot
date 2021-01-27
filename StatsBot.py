import discord
import time
import asyncio

messages = joined = 0
@client.event
async def on_message(message):
    await client.process_commands(message)

    global messages
    messages += 1 # counts each message sent in server

async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f: #counts number of messages sent onto a txt file
                f.write(f"Time: {int(time.time())}, Messages: {messages}\n")

                messages = 0

                await asyncio.sleep(480) #time interval to count each message, for example: counts messages every 480 seconds or 8 minutes

        except Exception as e:
            print(e)

    client.run(TOKEN)