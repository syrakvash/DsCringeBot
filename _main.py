
# @bot.command()
# async def join_voice(ctx):
#     member = await commands.MemberConverter().convert(ctx, '422380131521134604')
#     await ctx.send(member)
#     voice_state = None if not member.voice else member.voice.channel
#     if voice_state:
#         await member.voice.channel.connect()

# @bot.command()
# async def leave_voice(ctx):
#     member = await commands.MemberConverter().convert(ctx, '422380131521134604')
#     voice_state = None if not member.voice else member.voice.channel
#     if not voice_state:
#         await ctx.voice_client.disconnect()

# ID_DICT = {
#     'bomj_qqq': {'id': 422380131521134604, 'mp3': [
#         'ai_cringe_detection_bomj_qqq.mp3', 
#         'ai_cringe_detection_bomj_qqq_2.mp3', 
#         'ai_cringe_detection_bomj_qqq_3.mp3'
#         ]}, 
#     'lemingame': {'id': 699248660935999489, 'mp3': ['ai_cringe_detection_lemingame.mp3']}, 
#     'kambain': {'id': 273922920751955979, 'mp3': ['ai_cringe_detection_kambain.mp3']}, 
#     'zazulnitski': {'id': 709798855067303996, 'mp3': ['ai_cringe_detection_zazulnitski.mp3']},
#     'esq4444': {'id': 409394002283069440, 'mp3': ['ai_cringe_detection_esq4444.mp3']},
#     '.arma2ra': {'id': 328612957263101964, 'mp3': ['ai_cringe_detection_.arma2ra.mp3']},
#     'lil_mir': {'id': 329544067400728577, 'mp3': [
#         'ai_cringe_detection_lil_mir.mp3',
#         'ai_cringe_detection_lil_mir_2.mp3',
#         'ai_cringe_detection_lil_mir_3.mp3',
#         ]},
#     'jj93': {'id': 312346315063558144, 'mp3': ['ai_cringe_detection_jj93.mp3']},
#     'enabla': {'id': 326032689306140673, 'mp3': [
#         'ai_cringe_detection_enabla.mp3',
#         'ai_cringe_detection_enabla_2.mp3',
#         'ai_cringe_detection_enabla_3.mp3',
#         ]},
#     'gipsun9': {'id': 463301653970419712, 'mp3': ['ai_cringe_detection_gipsun9.mp3']},
#     }

# async def wait_for_stop_cycle_message(ctx, bot):
#     stop_cycle = False

#     def check(m):
#         return m.author == ctx.author and m.channel == ctx.channel

#     try:
#         message = await bot.wait_for("message", check=check, timeout=1)
#         stop_cycle = True if message.content.lower() == "/stop_cycle" else False
#         await ctx.send(f'STOP: {stop_cycle}')
#     except asyncio.TimeoutError:
#         ...

#     return stop_cycle


# async def connect_bot_to_channel(ctx, bot_connected_channel: discord.VoiceProtocol, member_voice_channel: discord.VoiceChannel) -> tuple[discord.VoiceProtocol, discord.VoiceClient, bool]:
#     bot_is_connected = False
    
#     try:
#         if not bot_connected_channel:
#             bot_connected_channel = await member_voice_channel.connect()
#             bot_is_connected = True
#         # else:
#         #     if bot_connected_channel.channel != member_voice_channel:
#         #         await bot_connected_channel.disconnect()
#         #         bot_connected_channel = await member_voice_channel.connect()
                
#         #         channel_changed = True
#     except discord.ClientException:
#         await ctx.send('error')

#     return bot_connected_channel, bot_connected_channel, bot_is_connected

# async def disconnect_bot_from_channel(bot_connected_channel: discord.VoiceProtocol):
#     if bot_connected_channel:
#         await bot_connected_channel.disconnect()
#         bot_connected_channel = None

#     return bot_connected_channel

# @bot.command()
# async def cycle(ctx):
#     stop_cycle = False
    
#     bot_connected_channel: discord.VoiceProtocol = None
        
#     while(not stop_cycle):
#         await asyncio.sleep(1)
#         stop_cycle = await wait_for_stop_cycle_message(ctx, bot)
#         if stop_cycle:
#             break
#         member: discord.Member = await commands.MemberConverter().convert(ctx, '422380131521134604')
#         voice_state = None if not member.voice else member.voice.channel
#         if voice_state:
#             bot_connected_channel, bot_connected_channel_client, bot_is_connected = await connect_bot_to_channel(ctx, bot_connected_channel, member.voice.channel)
#             if bot_is_connected:
#                 bot_connected_channel_client.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='q:\\ai_mp3.mp3'))
#                 while bot_connected_channel_client.is_playing():
#                     await asyncio.sleep(1)
#                 bot_connected_channel = await disconnect_bot_from_channel(bot_connected_channel)
#         else:
#             bot_connected_channel = await disconnect_bot_from_channel(bot_connected_channel)