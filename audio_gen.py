from gtts import gTTS
import os

from ai_gen import Patterns

MP3_FOLDER = 'mp3_temp'

def generate_audio_from_text(pattern, text):
    mp3_file_name = __get_file_location_name__(pattern)
    res = gTTS(text=text, lang='ru')
    res.save(__generate_file_name__(pattern))
    return mp3_file_name

def __get_file_location_name__(pattern):
    cwd = os.getcwd()
    mp3_temp_dir = os.path.join(cwd, MP3_FOLDER)
    mp3_file_name = __generate_file_name__(pattern)
    mp3_file_name = os.path.join(mp3_temp_dir, mp3_file_name)
    if not os.path.exists(mp3_temp_dir):
        os.mkdir(mp3_temp_dir)
    else:
        if os.path.exists(mp3_file_name):
            os.remove(mp3_file_name)
    return mp3_file_name

def __generate_file_name__(pattern: Patterns):
    return f"{pattern.name}.mp3"