import time

import speech_recognition as sr
from getaudio import record_audio

path = f"./chunks/chunk_s.wav"
record_audio(path, duration=8)
# time.sleep(4)
r = sr.Recognizer()
text = ""
with sr.AudioFile(path) as source:
    r.adjust_for_ambient_noise(source)
    audio_listened = r.record(source)
    # audio = r.record(source, offset=5, duration=15)
    try:
        text = r.recognize_google(audio_listened, language="de-DE")
    except Exception as e:
        print("Listening...")

print(text)