🎵 Discord Auto-Play Bot
This is a simple Discord bot built with discord.py that automatically connects to a voice channel on startup and plays a specified MP3 file at a set interval (cooldown). The bot also includes a command to leave the voice channel.

📋 Features
Automatically connects to a specified voice channel when the bot starts.

Plays a specified .mp3 file in a loop with a defined cooldown between plays.

Includes a command (!salir) to disconnect the bot from the voice channel.

Uses FFmpeg for audio playback.

🛠 Setup Instructions
1. Requirements
Python 3.8+

discord.py library

FFmpeg installed and available in your system PATH

Install dependencies:

bash
Copiar
Editar
pip install -U discord.py
2. Configuration
Edit the following variables in the Discord_Bot.py file:

python
Copiar
Editar
TOKEN = '(Your_Token)'  # Replace with your bot token
GUILD_ID = 1234567890   # Replace with your Discord server ID
VOICE_CHANNEL_ID = 1234567890  # Replace with your voice channel ID
MP3_FILE = r'C:\Users\(Path to your MP3 file).'  # Absolute path to your MP3 file
COOLDOWN = 30  # Cooldown in seconds between replays
Note: Ensure your bot has permission to connect to and speak in the target voice channel.

3. Run the Bot
bash
Copiar
Editar
python Discord_Bot.py
You should see output indicating the bot is connected and playing audio.

🧠 Usage
Once the bot is running:

It will auto-connect to the designated voice channel and begin playback.

It replays the MP3 file every COOLDOWN seconds if the file isn't currently playing.

Use the !salir command in any text channel the bot can read to make it leave the voice channel.

📌 Notes
Make sure FFmpeg is installed and working. You can download it from: https://ffmpeg.org/

The bot currently plays a local .mp3 file only. You can extend it to stream URLs or support playlists.

This script is meant for small personal servers. Consider using a proper queue/music handling library for larger implementations.
