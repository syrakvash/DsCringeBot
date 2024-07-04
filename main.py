import discord
from discord.ext import commands
import asyncio
import logging
import os

import ai_gen as AiTextGen
import audio_gen as AudioGen
from member_data import MembersInVoiceData

TOKEN = 'DSBOTTOKEN'
PREFIX = '/'

intents = discord.Intents().all()
cwd = os.getcwd()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if member.bot:
        return
    if (before.channel is None and after.channel) or (before.channel and after.channel):
        if before.channel is None and (before.self_mute or before.self_deaf):
            ...
        elif (after.afk or after.mute or after.self_mute or after.self_deaf or after.self_stream or after.self_video) \
            or (before.self_mute or before.self_deaf or before.self_stream or before.self_video):
            return
        member_in_voice_data = MembersInVoiceData()
        if after.channel is None:
            member_in_voice_data.remove_member(member)
        elif before.channel is None:
            member_in_voice_data.add_member(member)
        else:
            member_in_voice_data.update_member(member)
        text_to_speak = AiTextGen.generate_greetings_text(member.display_name)
        mp3_filename_to_speak = AudioGen.generate_audio_greeting(text_to_speak)
        await asyncio.sleep(1)
        await after.channel.connect()
        voice = discord.utils.get(bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=mp3_filename_to_speak))
        while voice.is_playing():
            await asyncio.sleep(1)
        await voice.disconnect()

bot.run(os.getenv(TOKEN), log_level=logging.DEBUG)