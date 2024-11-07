from gtts import gTTS
import os

from ai_gen import PATTERNS

MP3_CRINGE = 'crigne_output.mp3'
MP3_ACRINGE = 'acrigne_output.mp3'
MP3_GREETING = 'greeting_output.mp3'
MP3_BANNED = 'banned.mp3'
MP3_FOLDER = 'mp3_temp'

def generate_audio_from_text(pattern, text):
    mp3_file_name = __get_file_name__(pattern)
    res = gTTS(text=text, lang='ru')
    res.save(mp3_file_name)
    return mp3_file_name

def __get_file_name__(pattern):
    cwd = os.getcwd()
    mp3_temp_dir = os.path.join(cwd, MP3_FOLDER)
    match pattern:
        case PATTERNS.Greeting:
            mp3_file_name = MP3_GREETING
        case PATTERNS.Cringe:
            mp3_file_name = MP3_CRINGE
        case PATTERNS.ACringe:
            mp3_file_name = MP3_ACRINGE
        case PATTERNS.Banned:
            mp3_file_name = MP3_BANNED
    mp3_file_name = os.path.join(mp3_temp_dir, mp3_file_name)
    if not os.path.exists(mp3_temp_dir):
        os.mkdir(mp3_temp_dir)
    else:
        if os.path.exists(mp3_file_name):
            os.remove(mp3_file_name)
    return mp3_file_name