import os
import subprocess
import youtube_dl
from discord.ext.commands import Bot
print('Bot Started')

prefix = '.'
token = ''
client = Bot(command_prefix=prefix)
players = {}

@client.command(
                description='Pass a command to the Raspberry Pi terminal.',
                brief='Remote terminal access',
                pass_context=True,
                aliases=['t']
                )
async def terminal(context):
    os.system(context.message.content.replace('.terminal', '').replace('.t', ''))
    p = subprocess.Popen(context.message.content.replace('.terminal', '').replace('.t', ''), stdout=subprocess.PIPE, shell=True)
    output = p.communicate()
    await client.say(output)

@client.command(
                pass_context=True
                )
async def join(context):
    author = context.message.author
    channel = author.voice_channel
    await client.join_voice_channel(channel)

@client.command(
                pass_context=True,
                brief='Forces bot to leave the voice channel.',
                description='Forces bot to leave the voice channel it is currently in'
                )
async def leave(context):
    server = context.message.server
    vc = client.voice_client_in(server)
    await vc.disconnect()

@client.command(
                pass_context=True,
                brief='Play audio from YouTube.',
                description='Play audio from a YouTube URL'
                )
async def play(context, url):
    server = context.message.server
    vc = client.voice_client_in(server)
    player = await vc.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(
                pass_context=True
                )
async def EXAMPLE(context):
    author = context.message.author
    channel = author.voice_channel
    vc = await client.join_voice_channel(channel)
    player = vc.create_ffmpeg_player("PATH", after=vc.disconnect)
    player.start()


client.run(token)
