import discord
#import youtube_dl
from discord.ext import commands

client = commands.Bot(command_prefix="!")

# players = {}


# @client.event
# async def on_ready():
#     print("Bot is ready!")
#     print(client.user.name)
#     print(client.user.id)
#     print('------')


# @client.event
# async def on_message(message):
#     print("A message has sent")
#     await client.process_commands(message)


# @client.command(pass_context=True)
# async def join(ctx):
#     channel = ctx.message.author.voice.voice_channel
#     await client.join_voice_channel(channel)


# @client.command(pass_context=True)
# async def leave(ctx):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     await voice_client.disconnect()


# @client.command()
# async def hampus():
#     await client.say("Sanpus")


# @client.command(pass_context=True)
# async def play(ctx, url):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()

client.run("NTU3NTI1Nzk2NTc5NzA0ODUx.D3JnEQ.Sa04uCYytpCL2JZhEB_NdeYkjek")
