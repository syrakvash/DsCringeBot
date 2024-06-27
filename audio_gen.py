from gtts import gTTS
import os

def generate_audio_greeting(text):
    cwd = os.getcwd()
    mp3_temp_dir = os.path.join(cwd, 'mp3_temp')
    if not os.path.exists(mp3_temp_dir):
        os.mkdir(mp3_temp_dir)
    res = gTTS(text=text, lang='ru')
    mp3_file_name = os.path.join(mp3_temp_dir, 'output.mp3')
    if os.path.exists(mp3_file_name):
        os.remove(mp3_file_name)
    res.save(mp3_file_name)
    return mp3_file_name