from django.conf import settings

import os
import pyttsx3
import fitz
#from gtts import gTTS
from uuid import uuid4


def extract_text(filename):
    doc = fitz.open(filename)
    text = ""
    for pageNum in range(doc.page_count):
        page = doc[pageNum]
        text += page.get_text("text")
        print(text)
    return text



def store_audio_file(filepath, text, audio_rate=200, volume_level=1, audio_voice=1):
    """
    function to invoke TTS engine to speak the pdf text
    """

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',  voices[audio_voice].id)
    engine.setProperty('rate', audio_rate)
    engine.setProperty('volume', volume_level)
    engine.save_to_file(text, filepath)
    # engine.say(text)
    engine.runAndWait()
    engine.stop()
    """
    tts = gTTS(text, lang='en')

    tts.save(filepath)"""


def convert_pdf_to_audio(instance):
    text = extract_text(instance.pdf.path)
    audio_rate, volume_level, audio_voice = instance.audio_rate, instance.volume_level, instance.audio_voice
    file_name = uuid4()
    filepath = os.path.join(settings.BASE_DIR, f'media/recs/{file_name}.mp3')
    store_audio_file(filepath, text, audio_rate, volume_level, audio_voice)
    file_name = f'recs/{file_name}.mp3'
    return text, file_name
