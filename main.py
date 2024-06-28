import discord
from discord.ext import commands
import asyncio
import logging
# from random import randrange
import os

import ai_gen as AiTextGen
import audio_gen as AudioGen

TOKEN = 'DSBOTTOKEN'
PREFIX = '/'
REPLACEMYNICK = 'REPLACEMYNICK'
BASE_TEXT = f"""Человек с ником {REPLACEMYNICK} присоединяется к голосовому чату. 
Надо перевести ник на русский язык и придумать короткое смешное кринжовое приветствие.
Требования к приветствию: 
- короткое, смешное, кринжовое;
- только одно предложение;
- не более 4-5 слов;
- без одинарных и двойных ковычек;
- ник должен быть на русском языке;
- без слова ник.
"""

intents = discord.Intents().all()
cwd = os.getcwd()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if (before.channel is None and after.channel) or (before.channel and after.channel):
        member.prof
        if member.bot:
            return
        if before.channel is None and (before.self_mute or before.self_deaf):
            ...
        elif (after.afk or after.mute or after.self_mute or after.self_deaf or after.self_stream or after.self_video) \
            or (before.self_mute or before.self_deaf or before.self_stream or before.self_video):
            return
        base_text = BASE_TEXT.replace(REPLACEMYNICK, member.display_name)
        print(base_text)
        text_to_speak = AiTextGen.generate_greetings_text(base_text)
        mp3_filename_to_speak = AudioGen.generate_audio_greeting(text_to_speak)
        # if member.id in [
        #     values_list[k]
        #     for values_list in ID_DICT.values()
        #     for k in values_list.keys()
        #     if k == 'id'
        #     ]: 
        #     local_dict = {
        #         value_list:values_list[value_list]
        #         for values_list in ID_DICT.values()
        #         for value_list in values_list
        #         if values_list['id'] == member.id
        #         }
        await asyncio.sleep(1)
        await after.channel.connect()
        voice = discord.utils.get(bot.voice_clients)
        # voice.play(discord.FFmpegPCMAudio(executable="ffmpeg", source= os.path.join(cwd, f'mp3_files/{local_dict["mp3"][randrange(len(local_dict["mp3"]))]}')))
        voice.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=mp3_filename_to_speak))
        while voice.is_playing():
            await asyncio.sleep(1)
        await voice.disconnect()

bot.run(os.getenv(TOKEN), log_level=logging.DEBUG)