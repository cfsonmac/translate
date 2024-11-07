import speech_recognition as sr
import translators as ts

r = sr.Recognizer()
mic = sr.Microphone()
# mic = sr.Microphone(device_index=3)
# print(mic.list_working_microphones())
with mic as src:
    try:
        audio = r.listen(src)
        text = r.recognize_google(audio, language="de-DE")
        trans_text = ts.translate_text(text, "google", "auto", "zh")
        print(text, "\n", trans_text)
    except Exception as err:
        print(err)