import discord
from discord.ext import commands
import asyncio
import logging
import os

import discord.ext.commands

import ai_gen as AiTextGen
import audio_gen as AudioGen
import discord.ext
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
    member_in_voice_data = MembersInVoiceData()
    if after.channel is None:
        member_in_voice_data.remove_member(member)
        return
    if (before.channel is None and after.channel) or (before.channel and after.channel):
        if before.channel is None:
            member_in_voice_data.add_member(member)
        elif (after.afk or after.mute or after.self_mute or after.self_deaf or after.self_stream or after.self_video) \
            or (before.self_mute or before.self_deaf or before.self_stream or before.self_video):
            return
        else:
            member_in_voice_data.update_member(member)
        request, text_to_speak = AiTextGen.get_ai_response_text(pattern=AiTextGen.Patterns.GREETING, member_nick=member.display_name)
        member_in_voice_data.update_member_request_history(member, request, text_to_speak)
        mp3_filename_to_speak = AudioGen.generate_audio_from_text(AiTextGen.Patterns.GREETING, text_to_speak)
        await __bot_connect_to_channel_and_play__(after.channel, mp3_filename_to_speak)

@bot.command()
async def clmbr(ctx:discord.ext.commands.Context, *args):
    author = ctx.author
    member_in_voice_data = MembersInVoiceData()
    member_in_voice_data.add_member(author)
    if author.voice:
        req_permission = member_in_voice_data.check_request_permission(author)
        req_history = member_in_voice_data.get_member_request_history(author)
        if req_permission:
            pattern = AiTextGen.Patterns.CLMR
            request, text_to_speak = AiTextGen.get_ai_response_text(
                pattern=pattern, 
                data=' '.join(args), 
                reqs_history=req_history
                )
        else:
            pattern = AiTextGen.Patterns.BANNED
            request, text_to_speak = AiTextGen.get_ai_response_text(
                pattern=pattern, 
                member_nick=author.display_name, 
                reqs_history=req_history
                )
        member_in_voice_data.update_member_request_history(author, request, text_to_speak)
        mp3_filename_to_speak = AudioGen.generate_audio_from_text(pattern, text_to_speak)
        await __bot_connect_to_channel_and_play__(author.voice.channel, mp3_filename_to_speak)

@bot.command()
async def cringe(ctx:discord.ext.commands.Context, *args):
    author = ctx.author
    member_in_voice_data = MembersInVoiceData()
    member_in_voice_data.add_member(author)
    if author.voice:
        req_permission = member_in_voice_data.check_request_permission(author)
        req_history = member_in_voice_data.get_member_request_history(author)
        if req_permission:
            pattern = AiTextGen.Patterns.CRINGE
            request, text_to_speak = AiTextGen.get_ai_response_text(
                pattern=pattern, 
                data=' '.join(args), 
                reqs_history=req_history
                )
        else:
            pattern = AiTextGen.Patterns.BANNED
            request, text_to_speak = AiTextGen.get_ai_response_text(
                pattern=pattern, 
                member_nick=author.display_name, 
                reqs_history=req_history
                )
        member_in_voice_data.update_member_request_history(author, request, text_to_speak)
        mp3_filename_to_speak = AudioGen.generate_audio_from_text(pattern, text_to_speak)
        await __bot_connect_to_channel_and_play__(author.voice.channel, mp3_filename_to_speak)

@bot.command()
async def acringe(ctx:discord.ext.commands.Context, *args):
    author = ctx.author
    member_in_voice_data = MembersInVoiceData()
    member_in_voice_data.add_member(author)
    if author.voice:
        req_permission = member_in_voice_data.check_request_permission(author)
        req_history = member_in_voice_data.get_member_request_history(author)
        if req_permission:
            pattern = AiTextGen.Patterns.ACRINGE
            request, text_to_speak = AiTextGen.get_ai_response_text(
                pattern=pattern, 
                data=' '.join(args), 
                reqs_history=req_history
                )
        else:
            pattern = AiTextGen.Patterns.BANNED
            request, text_to_speak = AiTextGen.get_ai_response_text(
                pattern=pattern, 
                member_nick=author.display_name, 
                reqs_history=req_history
                )
        member_in_voice_data.update_member_request_history(author, request, text_to_speak)
        mp3_filename_to_speak = AudioGen.generate_audio_from_text(pattern, text_to_speak)
        await __bot_connect_to_channel_and_play__(author.voice.channel, mp3_filename_to_speak)

async def __bot_connect_to_channel_and_play__(channel: discord.VoiceChannel, mp3_filename_to_speak):
    await channel.connect()
    voice = discord.utils.get(bot.voice_clients)
    voice.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=mp3_filename_to_speak))
    while voice.is_playing():
        await asyncio.sleep(1)
    await voice.disconnect()

bot.run(os.getenv(TOKEN), log_level=logging.DEBUG)