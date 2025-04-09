import discord
from discord.ext import commands, tasks
import os
import asyncio


TOKEN = '(Your_Token)'  
GUILD_ID = 1234567890 # Replace with your server ID
VOICE_CHANNEL_ID = 1234567890 # Replace with your voice channel ID
MP3_FILE = r'C:\Users\(Path to your MP3 file).'
COOLDOWN = 30 #time of cooldown to the MP3 to play again

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'✅ Bot connected as {bot.user}')
    
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print("❌ Server Not Found.")
        return

    channel = guild.get_channel(VOICE_CHANNEL_ID)
    if not channel:
        print("❌ Voice Channel Not Found.")
        return


    if not discord.utils.get(bot.voice_clients, guild=guild):
        await channel.connect()
        print(f'🎤 Connected to {channel.name}')


    if not play_loop.is_running():
        play_loop.start()


@tasks.loop(seconds=COOLDOWN)
async def play_loop():
    voice_client = discord.utils.get(bot.voice_clients, guild=bot.get_guild(GUILD_ID))


    print(f'Buscando archivo en: {os.path.abspath(MP3_FILE)}')

    if voice_client and not voice_client.is_playing():
        if os.path.isfile(MP3_FILE):
            source = discord.FFmpegPCMAudio(MP3_FILE)
            voice_client.play(source)
            print(f'🎶 Replaying {MP3_FILE}')
        else:
            print(f'❌ File Not Found: {MP3_FILE}')


@bot.command(name='salir')
async def leave(ctx):
    if ctx.voice_client:
        play_loop.stop()
        await ctx.voice_client.disconnect()
        await ctx.send('👋 I disconnected from the Voice Channel.')
    else:
        await ctx.send('⚠️ I am not on any voice channel.')


bot.run(TOKEN)
